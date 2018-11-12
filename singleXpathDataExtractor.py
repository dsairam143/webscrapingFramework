#-*- coding:utf-8 -*-
import lxml.html
from lxml.html import tostring
from lxml.cssselect import CSSSelector
from bs4 import BeautifulSoup

def extractSinglePath(content, pPath):
    resp = content
    print(resp)
    productDict = dict()
    try:
        cssPath = pPath[2]
        tree = lxml.html.fromstring(resp)

        try:
            sel = CSSSelector(cssPath)
            result = lxml.html.tostring(sel(tree)[0])
        except:
            title = tree.xpath(cssPath)
            result = tostring(title[0])


        jsoup = BeautifulSoup(result)
        if pPath[1] == 'text':
            value = jsoup.text
        elif pPath[1] == 'href' or pPath[1] == 'a':
            value = jsoup.find('a')['href']
        elif pPath[1] == 'src' or pPath[1] == 'img':
            value = jsoup.find('img')['src']
        productDict[pPath[0]] = value
    except Exception as e:

        productDict[pPath[0]] = None

    return productDict





