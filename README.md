# Crawler
Implemented crawler using Breadth First Search Algorithm. Code can be found at https://github.com/venukarnati92/crawler/blob/master/crawler/crawler.py

# Bonus Questions

## Database
For dealing with hierarchical data in MySQL I have used Adjacency List Model.
In the adjacency list model, each item in the table contains a pointer to its parent(as shown in the below image).The topmost URL(RootNode) has a NULL value for its parent.
Data will be stored in the table as follows
```CREATE TABLE links(node_id INT AUTO_INCREMENT PRIMARY KEY, URL VARCHAR(2083) NOT NULL, Parent INT DEFAULT NULL```
Implementation can be found at https://github.com/venukarnati92/crawler/blob/master/crawler/crawler_DB.py

The snapshot of database schema 
<img width="453" alt="Screen Shot 2019-12-16 at 9 20 03 PM" src="https://user-images.githubusercontent.com/22748497/70969943-fb5f7b80-2051-11ea-8076-0dc8f328e30c.png">

## Multithreading
Inorder to implement multithreading, I have used threading module.Code can be found at https://github.com/venukarnati92/crawler/blob/master/crawler/crawler_multithreading.py

## Multiprocessing

Implemented multiprocessing

## How to extend it to distributed?


