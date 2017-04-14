#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Hang Yan'


def test():
    try:
        return "hehe"
    except Exception as e:
        print e
    else:
        print 'else hehe'


if __name__ == '__main__':
    print test()
