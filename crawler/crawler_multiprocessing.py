#!/usr/bin/env python3
from multiprocessing import Process, Queue, Manager
from bs4 import BeautifulSoup
import urllib.request as urlopen
from urllib.parse import urljoin
import queue # imported for using queue.Empty exception

def do_job(tasks_to_accomplish, tasks_that_are_done, shared_list):
    while True:
        try:
            '''
                try to get task from the queue. get_nowait() function will 
                raise queue.Empty exception if the queue is empty. 
                queue(False) function would do the same task also.
            '''
            url = tasks_to_accomplish.get_nowait()
            #url = tasks_to_accomplish.get()
        except queue.Empty:

            break
        else:
            '''
                if no exception has been raised, add the task completion 
                message to task_that_are_done queue
            '''
            print('saved html: {} : {} '.format(url, urlopen.urlopen(url).read().decode('utf-8')))
            tasks_that_are_done.put(url)
            html_page = urlopen.urlopen(url)
            soup = BeautifulSoup(html_page, "lxml")
            for link in soup.findAll('a'):
                print('saved link {} -> {}'.format(url, urljoin(url, link.get('href'))))
                if urljoin(url, link.get('href')) not in shared_list:
                    shared_list.append(urljoin(url, link.get('href')))
                    tasks_to_accomplish.put(urljoin(url, link.get('href')))
    return True

shared_list = Manager().list()
shared_list.append("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")

def main():
    number_of_processes = 4
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []

    #adding url to queue
    tasks_to_accomplish.put("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")
    
    # creating processes
    for w in range(number_of_processes):
        p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done, shared_list))
        processes.append(p)
        p.start()
        
    # completing process
    for p in processes:
        p.join()
           
    # print the output
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())

    return True

if __name__ == '__main__':
    main()