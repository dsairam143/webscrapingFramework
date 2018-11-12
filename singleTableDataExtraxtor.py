import requests
import lxml.html
from lxml.html import tostring
from bs4 import BeautifulSoup
from tabulate import tabulate
import re

def tableDataExtractor(htmlSource, xpath):
    root = lxml.html.fromstring(htmlSource)
    title = root.xpath(xpath)
    html_element = tostring(title[0])
    jsoup =  BeautifulSoup(html_element)

    if jsoup.find('table'):
        table = jsoup.find('table')

        trs = table.find_all('tr')
        nooftd = 0
        for tr in trs:
            tds = tr.find_all(re.compile('th|td'))
            if len(tds) > nooftd:
                nooftd = len(tds)
        trList = []
        for tr in trs:
            tds = tr.find_all(re.compile('th|td'))
            tdList = []
            for td in tds:
                colspan = 0
                try:
                    colspan = int(td['colspan'])
                except:
                    pass
                if colspan != 0:
                    tdList.append(td.text)
                    for k in range(colspan - 1):
                        tdList.append('')
                else:
                    tdList.append(td.text)

            trList.append(tdList)
        return trList