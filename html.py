#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib.request as urllib2
url="www.google.ro"
raspuns_server=urllib2.urlopen(url)
date=raspuns_server.read()
print(date)
print(date)