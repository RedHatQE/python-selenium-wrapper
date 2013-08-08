import logging, os, datetime
from selenium_wrapper_class import SeleniumWrapper
from selenium.common import WebDriverException

SE = SeleniumWrapper()

class ScreenShots(object):
    '''iterating over a driver with a side effect of taking screen shots'''
    def __init__(self, directory='./Screenshots'):
        self.directory = directory
        self._path_history = []
        self.log = logging.getLogger(self.__class__.__name__)

    @property
    def _next_path(self):
        '''give the path to a next screenshot'''
        return self.directory + "/" + datetime.datetime.now().isoformat() + ".png"

    def __next__(self):
        '''accessing next item takes a screenshot'''
        path = self._next_path
        self.log.debug("taking screenshot: %s" % path)
        try:
            if not SE.driver.get_screenshot_as_file(path):
                # try mkdir
                os.makedirs(self.directory)
                assert SE.driver.get_screenshot_as_file(path), "Taking screenshot"
            self._path_history.append(path)
        except WebDriverException as e:
            self.log.warning("unable to take screenshot %s: %s" % (path, e.message))
        return self._path_history[-1]

    next = __next__
    def __iter__(self):
        '''return the iterator over screenshots history'''
        return iter(self._path_history)

__all__ = [ScreenShots] 
