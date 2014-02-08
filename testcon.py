#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importing Needed Libraries
import MySQLdb as mdb
import feedparser
import sys
from testfnc import svdata

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
lls = [] # links list
cls = [] # content list
for m in range(lsrc):
	slng = len(data[m])
	for n in range(slng):
	# Atom XML RSS
		# titles
		tls.append(data[m].entries[n].title)
		# links
		lls.append(data[m].entries[n].feedburner_origlink)
		# content
		cls.append(data[m].entries[n].content)

	


# MySQL Connection

dbcon = mdb.connect('localhost','root','.staticx12','testdb')

# Cursor

with dbcon:
	dbcrs = dbcon.cursor()
	dbcrs.execute("DROP TABLE IF EXISTS Titles")
	dbcrs.execute("CREATE TABLE Titles(Id INT PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(255))")
	dbcrs.execute("INSERT INTO Titles(Title)",tls[0])

