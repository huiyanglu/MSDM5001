#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu

from bs4 import BeautifulSoup
import re
import  xml.dom.minidom

dom = xml.dom.minidom.parse('blocklist.xml')
dom2 = dom.toprettyxml()
soup = BeautifulSoup(dom2,'xml')
soup2 = soup.find('emItems')
soup3 = soup2.find_all('emItem')
Q1 = []
Q2 = []
for each in soup3:
    str_each = str(each)
    match = re.compile('<(.*)>')
    taglist = match.findall(str_each)[0]
    taglist2 = '<'+taglist+'>'
    match2 = re.compile('blockID="(.*)" id')
    blockID = match2.findall(taglist)[0]
    match3 = re.compile('[ig].*[0-9]')
    matched_blockID = match3.findall(blockID)
    if matched_blockID:
        Q1.append(taglist2)
    match_id = re.compile('id="(.*)"')
    id = match_id.findall(taglist)[0]
    match_id2 = re.compile('^[^\\\^/]+@[^\\\^/]+[.]+[^\\\^/]+$')
    id2 = match_id2.findall(id)
    if id2:
        Q2.append(taglist2)
print('Question 1: ')
for each in Q1:
    print(each)

print('Question 2:')
for each in Q2:
    print(each)