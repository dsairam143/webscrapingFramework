from selenium_browser import maks_browser

import requests
from homeBlogData import extractBlogData
from singleTableDataExtraxtor import tableDataExtractor
from singleXpathDataExtractor import extractSinglePath
from xpathsDataExtractor import xpathsData
import time

def getHomeBlogData(key, content, pathData, finalResult):
    print(pathData)
    if pathData.get('blogMainDivPath') and  pathData.get('blogPath') :
        finalResult[key] = extractBlogData(content, pathData.get('blogMainDivPath'), pathData.get('blogPath'))
    return finalResult

def getSingleTableDataExtractor(tableName, content, tablePath, finalResult):
    finalResult[tableName] = tableDataExtractor(content, tablePath)
    return finalResult

def getSingleXPathDataExtractor(key, content, singlePaths, finalResult):
    finalResult[key] = extractSinglePath(content, singlePaths)


def runner(driver, jsonFile, finalResult):
    for key, value in jsonFile.items():
        print(key)
        if 'clickButton' in key:
            driver.click_area_xpath(jsonFile.get(key))
        if 'input' in key:
            driver.sendKeys(jsonFile.get(key))
        if 'load' in key:
            driver.loadMore(jsonFile.get(key))
        if 'click' in key:
            driver.click_area_xpath(key, jsonFile.get(key))
        if 'dropDown' in key:
            driver.dropDown(jsonFile.get(key)[0], jsonFile.get(key)[1])
        if 'scroll' in key:
            driver.scrollDiv(jsonFile.get(key))
        if  'moveToBottomPage' in key:
            driver.moveToBottomPage()
        if 'sleep' in key:
            time.sleep(jsonFile.get(key))
        if 'dataFile' in key:
            #Extract the pagesource data
            time.sleep(3)
            finalResult[key] = xpathsData(driver.getBrowser().page_source, jsonFile.get(key))
        if 'forLoop' in key:
            print('inside for loop : ', finalResult)
            loopTags = value.get('path').split('>')
            loopResult = None
            if len(finalResult[value.get('dataFilePath')]):
                loop = finalResult
                for k in loopTags[:-1]:
                    loop = loop.get(k, {})
                print('After for loop = ', loop)
                if len(loop) != 0:
                    loopResult = loop
                    print('loop = ', loopResult)
            if loopResult:
                loopData = []
                for loo in loopResult:
                    try:
                        url = loo[value.get('path').split('>')[-1]]
                        if url[0] == '/':
                            url = value.get('attach')+url
                        elif url[:2] == '..':
                            url = value.get('attach') + url[2:]
                        print('url = ', url)
                        driver.loadBrowser(url)

                        lr  = xpathsData(driver.getBrowser().page_source, value.get('dataFile'))
                        print(lr)
                        loo['loopData'] = lr
                        loopData.append(loo)

                    except Exception as e:
                        print(e)

                finalResult[key] = loopData
    return finalResult


def SeleniumWebScraping():
    '''
        selenium_url: send url
        input_Area: pass values['Xpath', 'Value'],
        click_Area: click functin (pass xpath)
        dropDown_1: ['Xpath', 'Exact Value']
        sleep: Sleep Functionality
        moveToBottomPage_dddazsd : scrolling to bottom page
        scroll_dsfds : scroll a particular div,
        load_more: xpath

    '''
    jsonFile = {
        'selenium_url':'https://www.reuters.com/search/news?blob=bangalore+tech&sortBy=relevance&dateRange=pastYear',

        'dataFile_1':{
            "homeBlogData": {

                        "blogMainDivPath": "#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search", #Take Selector Only
                        "blogPath": [['Heading', 'text','#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search > div:nth-child(1) > div > h3'], #Take Selector Only
                                     ['Link', 'href','#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search > div:nth-child(1) > div > h3 > a'],
                                     ['Data', 'text', '#content > section:nth-child(5) > div > div.column1.col.col-10 > div.module > div > div.search-result-list.news-search > div:nth-child(1) > div > div']#Take Selector Only
                        ]
            },


        },
        'forLoop':{'dataFilePath':'dataFile_1',
                   'path':'dataFile_1>homeBlogData>Link',
                   'attach':'https://www.reuters.com',
                   'dataFile':{
                       "singlePath_1": ['Heading', 'text', '/html/body/div[4]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/h1']

                   }
                   }
    }



    if jsonFile.get('selenium_url'):
        driver = maks_browser()
        driver.loadBrowser(jsonFile.get('selenium_url'))
        finalResult= dict()
        result = runner(driver, jsonFile, finalResult)
        print('final Data = ', result)
        driver.closeBrowser()
SeleniumWebScraping()
