#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Hang Yan'


def get_page_source(url):
    import urllib2
    user_agent = """Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US)
  AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3"""
    headers = {'User-Agent': user_agent}
    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    return page


def get_soup(url):
    from bs4 import BeautifulSoup
    page = get_page_source(url)
    return BeautifulSoup(page)
