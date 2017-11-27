#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests,urllib
import argparse
import ast
class UrlFit():
  def __init__(self):
      self.URL = "https://api.url.fit/shorten"
  def Shorten(self,url):
    target = self.URL + "?long_url=" + urllib.quote_plus(url)
    resp = requests.get(target, headers={'User-Agent': 'Python Library 1.0'})
    return resp.json()

def main():
    parser = argparse.ArgumentParser(description='UrlFit -- shorten url')
    parser.add_argument('url', help='input url what you want to short')
    args = parser.parse_args()

    urlfit = UrlFit()
    short = urlfit.Shorten(str(args.url))
    print "https://url.fit/"+short["url"]
if __name__=="__main__":
    main()
