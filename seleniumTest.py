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
        'selenium_url':'https://www.bankrate.com/mortgage.aspx?type=newmortgage&propertyvalue=237500&loan=182400&perc=20&prods=1,2&fico=740&points=Zero&zipcode=56002&vet=NoMilitaryService&valoan=false&vad=false&fthb=false&propertytype=SingleFamily&propertyuse=PrimaryResidence&cashoutamount=0',
        'input_Area1':['//*[@id="property-location-input"]', '10004'],
        'input_Area2':['//*[@id="purchase-price"]', '125000'],
        'input_Area3':['//*[@id="property-downpayment-percentage"]', '20'],
        'click_Area':'//*[@id="mortgage-rate-table-app"]/div/div/div/div[1]/button',
        'sleep':3,
        'load_more':'/html/body/div[6]/div/div/div/div/div[2]/div[3]/table[1]/tfoot/tr/td/button',
        'load_more_2':'/html/body/div[6]/div/div/div/div/div[2]/div[3]/table[2]/tfoot/tr/td/button'

    }

    dataFile = {
        "homeBlogData": {

                    "blogMainDivPath": "table.offers-list:nth-child(1) > tbody:nth-child(2)", #Take Selector Only
                    "blogPath": [['BankName', 'attrs\img','table.offers-list:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > figure:nth-child(1) > img:nth-child(1)'], #Take Selector Only
                                 ['Apr', 'text','table.offers-list:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)'],
                                 ['Second', 'text', 'table.offers-list:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1)']#Take Selector Only
                    ]
        },
        "homeBlogData2": {

            "blogMainDivPath": "table.table:nth-child(2) > tbody:nth-child(2)",  # Take Selector Only
            "blogPath": [['BankName', 'attrs\img','table.table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > figure:nth-child(1) > img:nth-child(1)'],# Take Selector Only
                         ['Apr', 'text','table.table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)'],
                         ['Second', 'text','table.table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1)']# Take Selector Only
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


