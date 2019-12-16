#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request as urlopen
from urllib.parse import urljoin
import queue
import threading

#Get all the href's from the URL
def getLinks():
    while True:
        url = q.get()
        #get content from url
        #print('saved html: {} : {} '.format(url, urlopen.urlopen(url).read().decode('utf-8')))
        print(url)
        html_page = urlopen.urlopen(url)
        soup = BeautifulSoup(html_page, "lxml")
    
        #loop throgh all the links in a given url
        for link in soup.findAll('a'):
            #checking for absolute URL
            if link.get('href').startswith('http://') or link.get('href').startswith('https://'):
                #print reference info and absolute URL
                print('saved link {} -> {}'.format(url, link.get('href')))
                #avoid cycle calls
                if link.get('href') not in links:
                    with lock:
                        links.append(link.get('href'))
                    q.put(link.get('href'))
            #checking for relative URL        
            else:
                #print reference info and absolute URL
                #print('saved link {} -> {}'.format(url, urljoin(url, link.get('href'))))
                #avoid cycle calls
                if urljoin(url, link.get('href')) not in links:
                    with lock:
                        links.append(urljoin(url, link.get('href')))
                    q.put(urljoin(url, link.get('href')))
        q.task_done()

links = []
#adding root URL to the list
links.append("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")


num_worker_threads = 3
q = queue.Queue()
lock = threading.Lock()
threads = []

for i in range(num_worker_threads):
    t = threading.Thread(target=getLinks)
    t.start()
    threads.append(t)
    
#adding url to queue
q.put("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")


# block until all tasks are done
q.join()

print('stopping workers!')

# stop workers
for i in range(num_worker_threads):
    q.put(None)

for t in threads:
    t.join()

print(len(links) == len(set(links)))

