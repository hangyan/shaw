#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

__author__ = 'Hang Yan'


def caller_lineno():
    return sys._getframe(1).f_lineno


def caller_filename():
    return sys._getframe(1).f_code.co_filename


if __name__ == '__main__':
    def func():
        print caller_lineno()
        print caller_filename()
    func()
