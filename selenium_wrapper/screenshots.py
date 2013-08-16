import logging, os, datetime
from selenium_wrapper_class import SeleniumWrapper
from selenium.common.exceptions import WebDriverException
import time

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

    def _take_screenshot(self, path):
        if not SE.driver.get_screenshot_as_file(path):
            # try mkdir
            os.makedirs(self.directory)
            assert SE.driver.get_screenshot_as_file(path), "Taking screenshot"
        self._path_history.append(path)
        return self._path_history[-1]

    def __next__(self):
        '''accessing next item takes a screenshot'''
        path = self._next_path
        self.log.debug("taking screenshot: %s" % path)
        for i in range(4):
            # retry taking screenshots
            try:
                return self._take_screenshot(path)
            except WebDriverException as e:
                self.log.warning("...got: '%s'...retrying" % e)
            time.sleep(0.3)
        else:
            # last chance
            return self._take_screenshot(path)
            
            
    next = __next__
    def __iter__(self):
        '''return the iterator over screenshots history'''
        return iter(self._path_history)

__all__ = [ScreenShots] 
