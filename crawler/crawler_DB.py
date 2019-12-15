#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request as urlopen
from urllib.parse import urljoin
import pymysql

#Insert records to database
def insertToDB(childUrl, parentId):
    try:
        #insert records to DB
        cursor.execute("INSERT INTO category(URL, Parent) VALUES('{}',{})".format(childUrl, parentId))
    except pymysql.Error as exc:
        print("error inserting...\n {}".format(exc))
    links.append(childUrl)

#Get all the href's from the URL
def getLinks(url):
    html_page = urlopen.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")

    #loop throgh all the links in a given url
    for link in soup.findAll('a'):
        #checking for absolute URL
        if link.get('href').startswith('http://') or link.get('href').startswith('https://'):
            if link.get('href') not in links:
                childUrl= link.get('href')
                #get parent node_id
                cursor.execute("select node_id from category where url = '{}'".format(url))
                results = cursor.fetchall()
                for row in results:
                    parentId = row[0]
                #Insert records to database
                insertToDB(childUrl, parentId)
                #links.append(childUrl)
        #for relative URL        
        else:
            #print('saved link {} -> {}'.format(url, urljoin(url, link.get('href'))))
            if urljoin(url, link.get('href')) not in links:
                childUrl= urljoin(url, link.get('href'))
                #get parent node_id
                cursor.execute("select node_id from category where url = '{}'".format(url))
                results = cursor.fetchall()
                for row in results:
                    parentId = row[0]
                #Insert records to DB
                insertToDB(childUrl, parentId)
                #links.append(childUrl)
                
links = []
parentId = 0
#adding root URL to the list
links.append("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")

#database connection
db = pymysql.connect("localhost","crawler","crawler@123","TESTDB" )

# prepare a cursor object
cursor = db.cursor()

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS category")

#Create table
cursor.execute("CREATE TABLE category(node_id INT AUTO_INCREMENT PRIMARY KEY, URL VARCHAR(2083) NOT NULL, Parent INT DEFAULT NULL)")

#insert parent(root URL) record to DB
cursor.execute("INSERT INTO category(URL) VALUES('{}')".format(links[0]))

#loop through links across all pages
for i in links:
    #find all links in the page
    getLinks(i)

# Commit changes to the database
db.commit()
# disconnect from database
db.close()