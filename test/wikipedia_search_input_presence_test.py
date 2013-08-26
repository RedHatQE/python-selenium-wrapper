from selenium_wrapper import SE, restore_url, current_url


import unittest

class OpenPageTestCase(unittest.TestCase):
    search_input_locator = staticmethod(lambda : SE.find_element_by_name("search"))

    @classmethod
    def setUpClass(cls):
        SE.reset(driver='firefox', url="http://en.wikipedia.org")
        
    def setUp(self):
        self.verificationErrors = []
    
    def testSearchInputPresence(self):
        '''check input field presence'''
        self.assertIn(self.search_input_locator, SE)

    def testCurrentUrlCtx(self):
        '''check current url context manager works'''
        with current_url('https://google.com'):
            self.assertIn('google', SE.current_url)
        self.assertIn('wikipedia', SE.current_url)

    def testCurrentUrlCtxException(self):
        '''check current url context manager works in case of exception'''
        class CustomError(Exception):
            '''a custom error type to catch'''

        try:
            with current_url('https://google.com'):
                self.assertIn('google', SE.current_url)
                raise CustomError("as expected")
        except CustomError as e:
            pass

        self.assertIn('wikipedia', SE.current_url)
        

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
