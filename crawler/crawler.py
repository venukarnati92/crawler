#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request as urlopen
from urllib.parse import urljoin

#Get all the href's from the URL
def getLinks(url):
    #get content from url
    print('saved html: {} : {} '.format(url, urlopen.urlopen(url).read().decode('utf-8')))
    html_page = urlopen.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")

    #loop throgh all the links in a given url
    for link in soup.findAll('a'):
        #checking for absolute URL
        if link.get('href').startswith('http://') or link.get('href').startswith('https://'):
            #print reference info and absolute URL
            print('saved link {} -> {}'.format(url, link.get('href')))
            #avoid cycle calls
            if link.get('href') not in links:
                links.append(link.get('href'))
        #checking for relative URL        
        else:
            #print reference info and absolute URL
            print('saved link {} -> {}'.format(url, urljoin(url, link.get('href'))))
            #avoid cycle calls
            if urljoin(url, link.get('href')) not in links:
                links.append(urljoin(url, link.get('href')))

links = []
#adding root URL to the list
links.append("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")

#loop through links across all pages
for link in links:
    #find all links in the page
    getLinks(link)
