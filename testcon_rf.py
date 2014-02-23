#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importing Needed Libraries
import MySQLdb as mdb
import feedparser
import sys
from testfnc import svdata
import json


# Importing data from "sources.txt" file
source = 'sources1.txt'
sources = []

with open(source,'r') as file:
	for line in file:
		sources.append(line)

# Importing the RSS feeds
lsrc = len(sources)
data = []

# RSS Feed

for i in range(lsrc):
	data.append(feedparser.parse(sources[i]))

# Web Crawler


# Redudancy File Save [no connection / file save]
auxtxt = 'aux_prs.txt'
auxdata = 'aux_data.txt'
svdata(data, auxdata, auxtxt)

# Feed Analysis and JSON Transformation

#.# RSS FEED
tls = [] # titles list
tls_json = [] # titles json list
lls = [] # links list
lls_json = [] # links json list
cls = [] # content list
cls_json = [] # content json list
for m in range(lsrc):
	slng = len(data[m])
	for n in range(slng):
	# Atom XML RSS
		# titles
		tls.append(data[m].entries[n].title)
		tls_json.append(json.dumps(tls[n]))
		# links
		lls.append(data[m].entries[n].links[0].href)
		lls_json.append(json.dumps(lls[n]))
		# content
		cls.append(data[m].entries[n].summary)
		cls_json.append(json.dumps(cls[n]))

#.# Web Crawler


# MySQL Connection

dbcon = mdb.connect('localhost','root','.staticx12','testdb')

# Cursor
with dbcon:
	dbcrs = dbcon.cursor()
	# Creating the needed tables
	dbcrs.execute("DROP TABLE IF EXISTS TestFeeds")
	dbcrs.execute("CREATE TABLE TestFeeds(Id INT PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(255), Link VARCHAR(255), Content VARCHAR(2555))")

	len_json = len(tls_json)
	for p in range(len_json):
		dbcrs.execute("INSERT INTO TestFeeds(Title,Link,Content) VALUES(%s,%s,%s)", (tls_json[p],lls_json[p],cls_json[p]))
		


