from selenium.common.exceptions import NoSuchElementException
import logging, os, drivers
from datetime import datetime

log = logging.getLogger(__name__)

      

class SeleniumWrapper(object):
    # a singleton proxy to a default driver instance
    _instance = None
    _direct_attrs = ("_driver", "screenshots")
    screenshots = None

    def __new__(cls, *args, **kvargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kvargs)
            # clean-up the singleton at exit --- close the _driver
            import atexit
            atexit.register(cls._instance.__del__)
        return cls._instance

    def __init__(self):
        self._driver = None

    @property
    def driver(self):
        # for special driver use cases
        return self._driver

    @driver.setter
    def driver(self, aDriver):
        # for special driver use cases
        self._driver = aDriver

    def __getattr__(self, attrname):
        # proxy calls to the driver
        if attrname in self.__class__._direct_attrs:
            return self.__dict__[attrname]
        log.debug("proxying request %s to webdriver" % attrname)

        if self.screenshots is not None:
            log.debug("took screen shot %s" % next(self.screenshots))

        return getattr(self._driver, attrname)

    def __setattr__(self, attrname, value):
        # proxy calls to the driver
        if attrname in self.__class__._direct_attrs:
            self.__dict__[attrname] = value
            return
        setattr(self._driver, attrname, value)

    def __del__(self):
        # close & del the _driver
        try:
            self._driver.quit()
        except Exception:
            pass
        del(self._driver)

    def __contains__(self, locator):
        # locator should be a function
        # to examine the driver directly, use SeleniumWrapper().driver instead
        if callable(locator):
            try:
                locator()
                return True
            except NoSuchElementException:
                return False
        else:
            return locator in self._driver

    def reset(self, driver=None, url=None):
        # reset the driver
        # - if driver is None, setup a default one
        # - if driver is a string, it might be a driver name
        # - if url is not None, "get" it
        if self._driver is not None:
            try:
                self._driver.quit()
            except Exception as e:
                logging.log(logging.WARNING, "got: %s closing driver" % e)
                
        if driver is None:
            # let's use default
            self._driver = drivers.default_driver()
        elif isinstance(driver, str):
            # might be a driver name
            self._driver = drivers.get_driver_by_name(driver)
        else:
            # custom usage
            self._driver = driver

        if url is not None:
            self._driver.get(url)

__all__ = [SeleniumWrapper]
