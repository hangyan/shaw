#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from shaw.types import l

__author__ = 'Hang Yan'


class TestL(unittest.TestCase):

    def setUp(self):
        pass

    def test_identical(self):
        self.assertEqual(l.identical([1, 2, 3]), False)
        self.assertEqual(l.identical(['a', 'a', 'a']), True)
