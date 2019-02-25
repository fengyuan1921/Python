#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import os
paths = [r'D:/works/']
for path in paths:
    for filename in os.listdir(path):
        exname = filename.split('.')
        if exname[-1] == 'xlsx':
            worksheet = xlrd.open_workbook(path + filename)
            sheet = worksheet.sheet_by_index(0)
            nrows = sheet.nrows
            for i in range(nrows):
                values = sheet.row_values(i)
                print(values)
