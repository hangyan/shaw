#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from shaw.concurrence import process

__author__ = 'Hang Yan'


class TestConc(unittest.TestCase):

    def setUp(self):
        pass

    def test_process(self):
        def _f(item):
            return item * 10
        result = process([1,2,3], _f)
        self.assertEqual(result, [10,20,30])
