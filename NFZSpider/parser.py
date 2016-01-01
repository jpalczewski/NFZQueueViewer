#!/usr/bin/python
# -*- UTF-8 -*-
from openpyxl import load_workbook

wb = load_workbook("14_30112015.xlsx")
ws = wb.active

output = [set() for _ in xrange(11)]

for row in ws.rows:
    for i in xrange(11):
        output[i].add(row[i].value)

for i in xrange(11):
    print len(output[i])
