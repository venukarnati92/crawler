#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request as urlopen
from urllib.parse import urljoin
import re

def getLinks(url):
    html_page = urlopen.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")

    #for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print('saved html: {} {} '.format(url, soup.findAll('a')))
    for link in soup.findAll('a'):
        if link.get('href').startswith('http://') or link.get('href').startswith('https://'):
            print('saved link {} -> {}'.format(url, link.get('href')))
            if link.get('href') not in links:
                links.append(link.get('href'))
        else:
            print('saved link {} -> {}'.format(url, urljoin(url, link.get('href'))))
            if urljoin(url, link.get('href')) not in links:
                links.append(urljoin(url, link.get('href')))

links = []
links.append("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")
for i in links:
    getLinks(i)
