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

if __name__ == '__main__':
    jsonFile = {
        'selenium_url':'http://www.comparefirst.sg/wap/homeEvent.action',
        'click_Area1':'/html/body',
        'click_Area3': '/html/body',
        'click_area4':'/html/body/div[5]/div/div[4]/a[1]',
        'input_Area':['//*[@id="date"]', '01/07/1973'],
        'click_Area5': '/html/body',
        'click_Area2':'//*[@id="select2-chosen-9"]',
        'dropDown_1':['//*[@id="select2-results-9"]', 'To Age 65'],
        'click_area11':'//*[@id="s2id_SADCIPTermAn"]',
        'dropDown_2':['//*[@id="select2-results-4"]', 'S$ 300,000'],
        'click_are111':'//*[@id="s2id_sortNonWLGroup"]',
        'dropDown_333':['//*[@id="select2-results-16"]', 'Premium (Lowest - Highest)'],
        'click_sdasdsa':'//*[@id="viewPopup"]',
        'click_dfdf':'//*[@id="iUnderstant"]',
        'click_dfdfsdfgfdg': '//*[@id="iUnderstant"]',
        'sleep':3,
        'moveToBottomPage_dddazsd': 'moveToBottomPage',
        'scroll_dsfds':'//*[@id="result_container"]',
    }

    dataFile = {
        "homeBlogData": {

                    "blogMainDivPath": "#result_container", #Take Selector Only
                    "blogPath": [['Heading', 'text','li.ui-draggable:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1)'], #Take Selector Only
                                 ['Data', 'text','li.ui-draggable:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'] #Take Selector Only
                    ]
        },

    }

    if jsonFile.get('selenium_url'):
        driver = maks_browser()
        driver.loadBrowser(jsonFile.get('selenium_url'))

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
        #Extract the pagesource data
        time.sleep(3)
        result = xpathsData(driver.getBrowser().page_source, dataFile)
        print(result)


