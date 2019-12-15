#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request as urlopen
from urllib.parse import urljoin
import pymysql

#Insert records to DB
def insertToDB(url, parentId):
    try:
        # Execute the SQL command
        cursor.execute("INSERT INTO category(URL, Parent) VALUES('{}',{})".format(url, parentId))
    except pymysql.Error as exc:
        print("error inserting...\n {}".format(exc))

#Get all the href's from the URL
def getLinks(url):
    #print('saved html: {} : {} '.format(url, urlopen.urlopen(url).read().decode('utf-8')))
    html_page = urlopen.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")

    #loop throgh all the links in a given url
    for link in soup.findAll('a'):
        #For absolute URL
        if link.get('href').startswith('http://') or link.get('href').startswith('https://'):
            #print('saved link {} -> {}'.format(url, link.get('href')))
            if link.get('href') not in links:
                dbURL= link.get('href')
                cursor.execute("select node_id from category where url = '{}'".format(url))
                results = cursor.fetchall()
                for row in results:
                    parentId = row[0]
                insertToDB(dbURL, parentId)
                links.append(link.get('href'))
        #for relative URL        
        else:
            #print('saved link {} -> {}'.format(url, urljoin(url, link.get('href'))))
            if urljoin(url, link.get('href')) not in links:
                dbURL= urljoin(url, link.get('href'))
                cursor.execute("select node_id from category where url = '{}'".format(url))
                results = cursor.fetchall()
                for row in results:
                    parentId = row[0]
                #print(url, dbURL, parentId)
                insertToDB(dbURL, parentId)
                links.append(urljoin(url, link.get('href')))
                
links = []
parentId = 0
links.append("https://storage.googleapis.com/crawler-interview/e0228c0d-e5fe-4af5-87c7-6e41fd82a6b3.html")

# Open database connection
db = pymysql.connect("localhost","crawler","crawler@123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS category")

#Create table
cursor.execute("CREATE TABLE category(node_id INT AUTO_INCREMENT PRIMARY KEY, URL VARCHAR(2083) NOT NULL, Parent INT DEFAULT NULL)")

#insert parent record to DB
cursor.execute("INSERT INTO category(URL) VALUES('{}')".format(links[0]))

#go through all the links
for i in links:
    getLinks(i)

# Commit changes in the database
db.commit()
# disconnect from server
db.close()
