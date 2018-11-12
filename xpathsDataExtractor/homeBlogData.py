import lxml.html
import re
from lxml.cssselect import CSSSelector
from bs4 import BeautifulSoup

def extractBlogData(content, xpath, productPath):
    print(xpath, productPath)
    resp = content
    tree = lxml.html.fromstring(resp)
    sel = CSSSelector(xpath)

    divs = BeautifulSoup(lxml.html.tostring(sel(tree)[0])).find('body').findNext()
    pProductList = []
    for div in divs.findChildren(recursive=False):
        div = str(div)
        productDict = dict()
        for pPath in productPath:
            try:
                cssPath = pPath[2].replace(xpath, '').strip(' >')
                test = [re.sub(':.*', '', k) for k in cssPath.split('>')]
                cssPath = '>'.join(test)
                tree = lxml.html.fromstring(div)
                sel = CSSSelector(cssPath)
                result = lxml.html.tostring(sel(tree)[0])
                jsoup = BeautifulSoup(result)
                if pPath[1] == 'text':
                    value = jsoup.text.strip()
                elif pPath[1] == 'href' or pPath[1] == 'a':
                    value = jsoup.find('a')['href']
                elif pPath[1] == 'src' or pPath[1] == 'img':
                    value = jsoup.find('img')['src']
                elif 'attrs' in pPath[1]:
                    value = jsoup.find(pPath[1].split('\\')[-1]).attrs
                productDict[pPath[0]] = value
            except Exception as e:
                productDict[pPath[0]] = None
        pProductList.append(productDict)

    return pProductList



# jsonFile = {"homeBlogData":{
#     'url':"https://www.dailysabah.com/search?key=politics",
#     "blogMainDivPath":"body > section > form > div > div.table > div.right > div.searchList > ul",
#     "blogPath":[['Heading', 'text', 'body > section > form > div > div.table > div.right > div.searchList > ul > li:nth-child(6) > a:nth-child(3) > span > strong']]
# }
# }
#
#
# productData = [['Heading', 'text', 'body > section > form > div > div.table > div.right > div.searchList > ul > li:nth-child(6) > a:nth-child(3) > span > strong']
#                ]
# tableData = extractBlogData('https://www.dailysabah.com/search?key=politics','body > section > form > div > div.table > div.right > div.searchList > ul', productData)