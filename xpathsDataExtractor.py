import requests
from homeBlogData import extractBlogData
from singleTableDataExtraxtor import tableDataExtractor
from singleXpathDataExtractor import extractSinglePath

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

def xpathsData(content, jsonFile):


    # jsonFile = {
    #     "mainUrl": "https://www.w3schools.com/html/html_tables.asp",
    #     "homeBlogData": {
    #         'url': "https://www.reuters.com/search/news?blob=bangalore+tech&sortBy=relevance&dateRange=pastYear",
    #         "blogMainDivPath": "#main > ul", #Take Selector Only
    #         "blogPath": [['Heading', 'text','#main > ul > li:nth-child(1)'], #Take Selector Only
    #                      ['Data', 'text','#main > ul > li:nth-child(1) > code'] #Take Selector Only
    #         ]
    #
    #     },
    #     "tableData":'//*[@id="main"]/div[3]/div',  #Take Xpaths Only
    #     "singlePath":['Heading', 'text', '//*[@id="main"]/h2[1]'] #take Xpaths or selectors
    #
    #
    # }


    finalResult = dict()


    for key,value in jsonFile.items():

        if 'homeBlogData' in key:
            if jsonFile.get(key):
                getHomeBlogData(key, content, jsonFile.get(key), finalResult)

        if 'tableData' in key:
            if jsonFile.get(key):
                getSingleTableDataExtractor(key, content, jsonFile.get(key), finalResult)

        if 'singlePath' in key:
            if jsonFile.get(key):
                getSingleXPathDataExtractor(key, content, jsonFile.get(key), finalResult)
    return finalResult