from selenium_wrapper import SE


import unittest

class OpenPageTestCase(unittest.TestCase):
    search_input_locator = staticmethod(lambda : SE.find_element_by_name("search"))

    @classmethod
    def setUpClass(cls):
        SE.reset(driver='firefox', url="http://en.wikipedia.org")
        
    def setUp(self):
        self.verificationErrors = []
    
    def testSearchInputPresence(self):
        self.assertIn(self.search_input_locator, SE)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
