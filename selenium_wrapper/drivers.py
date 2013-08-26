from selenium.webdriver import PhantomJS, Firefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

def get_phantom_driver():
    # we'd like to
    # - accept untrusterd certs
    return PhantomJS('phantomjs', service_args=['--webdriver-loglevel', 'DEBUG', '--web-security', 'false', '--ignore-ssl-errors', 'yes'])

def get_firefox_driver():
    # we'd like to
    # - accept untrusterd certs
    # - automatically save downloads to cwd/Downloads
    profile = FirefoxProfile()
    profile.accept_untrusted_cert = True
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", os.getcwd() + "/Downloads")
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.panel.shown", False)
    profile.set_preference("browser.download.show_plugins_in_list", False)
    profile.set_preference("browser.download.closeWhenDone", True)
    profile.set_preference("browser.download.useWindow", False)
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk",
        ",".join([
            "application/octet-stream",
            "application/zip",
            "application/gzip",
            "application/bzip2",
            "application/x-tar"
        ])
    )

    return Firefox(profile)

name_driver_map = {
    'firefox': get_firefox_driver,
    'phantom': get_phantom_driver
}

def get_driver_by_name(name):
    if name in name_driver_map:
        return name_driver_map[name]()
    raise RuntimeError("wrong driver name: %s" % name)


# default driver is firefox
default_driver = get_firefox_driver

