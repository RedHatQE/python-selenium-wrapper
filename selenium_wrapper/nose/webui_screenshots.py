import logging, os, datetime
from selenium_wrapper import SE
from selenium_wrapper.screenshots import ScreenShots
from nose.plugins import Plugin

log = logging.getLogger(__name__)

class WebuiScreenshots(Plugin):
    '''Take Screenshots of each testcase steps in a separate directory'''
    dirname = os.getcwd() + "/" + 'Screenshots' + '/' + datetime.datetime.now().isoformat()
    enabled = True
    keep_passing_screenshots = False

    def options(self, parser, env=os.environ):
        #FIXME figure out any custom save options; dir...
        super(WebuiScreenshots, self).options(parser, env=env)
        env_opt = 'NOSE_KEEP_PASSING_SCREENSHOTS'
        parser.add_option('--keep-passing-screenshots', action='store_true',
                          dest='keep_passing_screenshots', default=env.get(env_opt, False),
                          help='Disable cleaning of passing testcases screen shots')

    def screenshots_directory(self, test, failed=False, error=False):
        '''generate proper test case screen shot directory name'''
        fmt_in = (self.dirname, str(test.id()))
        if error:
            return "%s/ERROR_%s" % fmt_in
        if failed:
            return "%s/FAILED_%s" % fmt_in
        return "%s/%s" % fmt_in

    def configure(self, options, conf):
        super(WebuiScreenshots, self).configure(options, conf)

        if not self.enabled or not self.can_configure:
            return

        if getattr(options, 'keep_passing_screenshots', False):
            self.keep_passing_screenshots = True

    def beforeTest(self, test):
        '''set separate screenshot directory for each test case'''
        SE.screenshots = ScreenShots(self.screenshots_directory(test))

    def addSuccess(self, test):
        '''clean passing test screenshots'''
        if self.keep_passing_screenshots:
            return

        try:
            map(lambda x: os.remove(x), SE.screenshots)
            os.removedirs(self.screenshots_directory(test))
        except OSError as e:
            # e.g. non-empty screenshots_directory
            log.warning("got '%s' cleaning '%s'" % (e, self.screenshots_directory(test)))

    def formatError(self, test, err):
        '''rename the testcase directory to denote the error'''
        try:
            os.renames(self.screenshots_directory(test), self.screenshots_directory(test, error=True))
        except OSError as e:
            # may happen in case of a module failure  --> no screenshots are present
            log.warning("got '%s' formating error: '%s'" % (e, err))

    def formatFailure(self, test, err):
        '''rename the testcase directory to denote the failure'''
        try:
            os.renames(self.screenshots_directory(test), self.screenshots_directory(test, failed=True))
        except OSError as e:
            # happens e.g. when a test case failed without taking any screenshots
            log.warning("got '%s' formating failure: '%s'" % (e, err))
