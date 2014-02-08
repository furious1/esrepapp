#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle

class Company:
    def __init__(self, name, value):
        self.name = name
        self.value = value

with open('company_data.pk', 'wb') as output:
    company1 = Company('banana', 40)
    pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)

    company2 = Company('spam', 42)
    pickle.dump(company2, output, pickle.HIGHEST_PROTOCOL)

company1 = None
company2 = None

with open('company_data.pk', 'rb') as input:
    company1 = pickle.load(input)
    print company1.name
    # banana
    print company1.value
    # 40

    company2 = pickle.load(input)
    print company2.name
    # spam
    print company2.value
    # 42
