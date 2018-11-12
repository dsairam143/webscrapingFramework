import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
class maks_browser:
    def loadBrowser(self, url):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(url)

    def getBrowser(self):
        return self.driver

    def click_area_xpath(self, key, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.click()
        except Exception as error:
            try:
                self.driver.find_element_by_xpath(xpath).click()
            except Exception as e:
                print(key, e)
            print(key,error)
    def sendKeys(self, pathAndKey):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pathAndKey[0]))
        )
        element.clear()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pathAndKey[0]))
        )
        element.send_keys(pathAndKey[1])
        element.send_keys(Keys.RETURN)

    def loadMore(self, path):
        try:
            for k in range(10):
                print(k)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, path))
                )
                element.click()
        except Exception as e:
            print(e)

    def dropDown(self, xpath, check_value):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        jsoup = BeautifulSoup(element.get_attribute('innerHTML'))
        targetId = 0
        print(jsoup.find('body').findChildren(recursive=False))
        for id, value in enumerate(jsoup.find('body').findChildren(recursive=False)):
            print(value.text.strip())
            if check_value == value.text.strip():
                print(value)
                targetId =id
                print(xpath+'/'+value.name+'['+str(id)+']')
                self.click_area_xpath('dropdown',xpath+'/'+value.name+'['+str(id+1)+']')
        print('targetId', targetId)

    def scrollDiv(self, xpath):
        try:
            eula = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', eula)
        except Exception as e:
            print(e)
    def moveToBottomPage(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            print(e)
    def closeBrowser(self):
        self.driver.close()

# driver = maks_browser()
# driver.loadBrowser('https://www.w3schools.com/html/html_tables.asp')
# driver.click_area_xpath('//*[@id="main"]/div[2]/a[2]')
# print(driver.getBrowser().page_source)
# driver.closeBrowser()
