#!/usr/bin/python
# -*- coding: utf-8 -*-

source = 'sources.txt'

sources = []
with open(source,'r') as file:
#	read_data = file.read()
	for line in file:
		sources.append(line)

print sources[0]
