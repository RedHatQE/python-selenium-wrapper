from selenium_wrapper import SE


import sys, unittest, re, time, os.path, logging, nose

class OpenPageTestCase(unittest.TestCase):
    search_input_locator = staticmethod(lambda : SE.find_element_by_name("search"))
    def setUp(self):
        self.log = logging.getLogger("wikipedia.search.input.presence.test")
        self.verificationErrors = []
        SE.reset(url="http://en.wikipedia.org")
    
    def testSearchInputPresence(self):
        self.assertIn(self.search_input_locator, SE)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
