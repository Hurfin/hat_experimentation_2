# -*- coding: utf-8 -*-
# !/usr/bin/env python

from urllib import request
from urllib import parse
import re
import time

def getOrgsName():
    orgslist = []
    with open(r"E:\pythonCode\RJ_experimentation_1\Data\uni_orgs.txt", "r", encoding='utf-8') as f:
        for org in f:
            org = org.strip()
            orgslist.append(org)
    return orgslist
    pass
url_baike = "https://baike.baidu.com/item/"

headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/62.0.3202.94 Safari/537.36")
opener = request.build_opener()
opener.addheaders = [headers]
request.install_opener(opener)
orgNameList = getOrgsName()
f = open(r"E:\pythonCode\RJ_experimentation_1\Data\orgName_englishName.txt", "a+", encoding='utf-8')
for orgName in orgNameList:
    url = url_baike + parse.quote(orgName)
    data = ""
    try:
        data = request.urlopen(url).read().decode('utf-8')
    except Exception as e:
        page = e.partial
        data = page.decode('utf-8')

    pat = """<dt class="basicInfo-item name">英文名</dt>\s*<dd class="basicInfo-item value">\s*(.+)\s*</dd>"""
    pat1 = """<dt class="basicInfo-item name">外文名</dt>\s*<dd class="basicInfo-item value">\s*(.+)\s*</dd>"""
    pat2 = """<dt class="basicInfo-item name">外文名称</dt>\s*<dd class="basicInfo-item value">\s*(.+)\s*</dd>"""
    englishName = re.compile(pat).findall(data)
    englishName1 = re.compile(pat1).findall(data)
    englishName2 = re.compile(pat2).findall(data)
    englishName = englishName + englishName1 + englishName2
    print(orgName, englishName)
    f.write(orgName+"\t"+"\t".join(englishName)+"\n")
    time.sleep(2)
f.close()



# from urllib import request
#
# target_url = 'http://www.biquge9.com/'
# result = request.urlopen(target_url)
# print(result.read().decode('utf-8'))