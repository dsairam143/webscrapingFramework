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

if __name__ == "__main__":


    # jsonFile = {
    #     "mainUrl": "https://www.w3schools.com/html/html_tables.asp",
    #     "homeBlogData": {
    #         'url': "https://www.reuters.com/search/news?blob=bangalore+tech&sortBy=relevance&dateRange=pastYear",
    #         "blogMainDivPath": "#main > ul",
    #         "blogPath": [['Heading', 'text','#main > ul > li:nth-child(1)'],
    #                      ['Data', 'text','#main > ul > li:nth-child(1) > code']
    #         ]
    #
    #     },
    #     "tableData":'//*[@id="main"]/div[3]/div',
    #     "singlePath":['Heading', 'text', '//*[@id="main"]/h2[1]']
    #
    #
    # }

    jsonFile = {
        "mainUrl": "https://www.w3schools.com/html/html_tables.asp",
        "homeBlogData_sideNavigation": {
            'url': "https://www.reuters.com/search/news?blob=bangalore+tech&sortBy=relevance&dateRange=pastYear",
            "blogMainDivPath": "#leftmenuinnerinner",
            "blogPath": [['Heading', 'text', '#leftmenuinnerinner > a:nth-child(3)'],
                         ['Link', 'href', '#leftmenuinnerinner > a:nth-child(3)']
                         ]

        },
        "singlePath_tableName":['Heading', 'text', '//*[@id="main"]/div[3]/h3'],
        "tableData_firstTable":'//*[@id="main"]/div[3]/div',

        "singlePath_ChapterSummery":['Heading', 'text', '//*[@id="main"]/h2[11]'],

        "homeBlogData_ulData":{
            "blogMainDivPath":"#main > ul",
            "blogPath":[['Heading', 'text', '#main > ul > li:nth-child(1)'],
                        ['SubHeading', 'text', '#main > ul > li:nth-child(1) > code']]
        }
        # "tableData": '//*[@id="main"]/div[3]/div',
        # "singlePath": ['Heading', 'text', '//*[@id="main"]/h2[1]']

    }
    finalResult = dict()
    content = requests.get(jsonFile.get('mainUrl')).content

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
    print(finalResult)