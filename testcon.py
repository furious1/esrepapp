#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importing Needed Libraries
import MySQLdb as mdb
import feedparser
import sys
from testfnc import svdata
import json


# Importing data from "sources.txt" file
source = 'sources.txt'
sources = []

with open(source,'r') as file:
	for line in file:
		sources.append(line)

# Importing the RSS feeds
lsrc = len(sources)
data = []



for i in range(lsrc):
	data.append(feedparser.parse(sources[i]))



# Redudancy File Save [no connection / file save]
auxtxt = 'aux_prs.txt'
auxdata = 'aux_data.txt'
svdata(data, auxdata, auxtxt)

# Feed Analysis

#.# Declaration lists

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
		lls.append(data[m].entries[n].feedburner_origlink)
		lls_json.append(json.dumps(lls[n]))
		# content
		cls.append(data[m].entries[n].content)
		cls_json.append(json.dumps(cls[n]))

print len(cls_json[0])
print cls_json[0]

# MySQL Connection

dbcon = mdb.connect('localhost','root','.staticx12','testdb')

# Cursor
qwe = tls_json[0]
with dbcon:
	dbcrs = dbcon.cursor()
	# Creating the needed tables
	dbcrs.execute("DROP TABLE IF EXISTS Feeds")
	dbcrs.execute("CREATE TABLE Feeds(Id INT PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(255), Link VARCHAR(255))")

	len_json = len(tls_json)
	for p in range(len_json):
		dbcrs.execute("INSERT INTO Feeds(Title,Link) VALUES(%s,%s)", (tls_json[p],lls_json[p]))
		


