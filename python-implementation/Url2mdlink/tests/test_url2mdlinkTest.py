# -*- coding: utf-8 -*-

import unittest
from Url2mdlink.url2mdlink.url2mdlink import transform

FAILURE = 'incorrect value'


class Url2mdlinkTest(unittest.TestCase):
    def test_google(self):
        url = "https://www.google.com"
        actual = transform(url)
        expected = "[Google](https://www.google.com)"
        self.assertEqual(actual, expected, FAILURE)

    def test_abehiroshi(self):
        url = "http://abehiroshi.la.coocan.jp"
        actual = transform(url)
        expected = "[阿部寛のホームページ](http://abehiroshi.la.coocan.jp)"
        self.assertEqual(actual, expected, FAILURE)
