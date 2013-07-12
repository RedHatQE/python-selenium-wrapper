#!/usr/bin/env python
import sys, unittest, re, time, os.path, logging, nose, yaml

from pageobjects.login import LoginPageObject
from selenium_wrapper import SE
from config import load_sam


class SamLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.sam = load_sam()
        self.log = logging.getLogger("splice.login")
        self.verificationErrors = []
        SE.reset(url=self.sam.url)

    def testLogin(self):
        lpo = LoginPageObject()
        lpo.username = self.sam.username
        lpo.password = self.sam.password
        lpo.submit()

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    nose.main()
