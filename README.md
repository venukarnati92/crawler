# Crawler
Implemented crawler using Breadth First Search Algorithm. Code can be found at https://github.com/venukarnati92/crawler/blob/master/crawler/crawler.py

# Bonus Questions

## Database:
For dealing with hierarchical data in MySQL I have used Adjacency List Model.
In the adjacency list model, each item in the table contains a pointer to its parent(as shown in the below image).The topmost URL(RootNode) has a NULL value for its parent.
Data will be stored in the table as follows
```CREATE TABLE links(node_id INT AUTO_INCREMENT PRIMARY KEY, URL VARCHAR(2083) NOT NULL, Parent INT DEFAULT NULL```
Implementation can be found at https://github.com/venukarnati92/crawler/blob/master/crawler/crawler_DB.py

The snapshot of database schema 
<img width="453" alt="Screen Shot 2019-12-16 at 9 20 03 PM" src="https://user-images.githubusercontent.com/22748497/70969943-fb5f7b80-2051-11ea-8076-0dc8f328e30c.png">

## Multithreading:
Inorder to implement multithreading, I have used threading module.Code can be found at https://github.com/venukarnati92/crawler/blob/master/crawler/crawler_multithreading.py

## Multiprocessing:

For multiprocessing implementation, I have used multiprocessing module.Code can be found at
https://github.com/venukarnati92/crawler/blob/master/crawler/crawler_multiprocessing.py

## How to extend it to distributed?

For extending the code to distribution we can use Ray which is an open source library for writing parallel and distributed Python.
To turn a Python function getLinks() in our code into a “remote function”, we can declare the function with the @ray.remote decorator. Then function invocations via getLinks.remote() will immediately return futures (a future is a reference to the eventual output), and the actual function execution will take place in the background (we refer to this execution as a task).
```
@ray.remote
#Get all the href's from the URL
def getLinks(url):
    html_page = urlopen.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")```
