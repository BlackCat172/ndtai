import sys
import time
# from sys import platform
#!/usr/bin/python

# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pygologin.gologin import GoLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import json

gl = GoLogin({
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmU3YzcxM2U5YjZlMGM1OWY4OWRlZmEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MmU3Yzc1NDM2OTZkYmFhODAyMzcxNTEifQ.lYJNWu1xLgAXIbym5uuOWgOP6yoFtfSFsHVmY1-OvTI",
    "profile_id": "62e7c713e9b6e025ee89defc",
    # "port": random_port
})
chrome_driver_path = "/Users/nguyenductai/Downloads/chromedriver"
debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
# ----------------------------
dict={}
driver.get("https://vnexpress.net/goc-nhin")
tmp=len(driver.find_elements(By.XPATH,"/html/body/section[4]/div/div[2]/div/article"))
f=open("result.txt","w")

for i1 in range(1,tmp+1):
    #driver.get("https://vnexpress.net/goc-nhin")
    dict2={}
    title_xpath='/html/body/section[4]/div/div[2]/div/article['+str(i1)+']/h3/a'
    description_xpath='/html/body/section[4]/div/div[2]/div/article['+str(i1)+']/p[1]/a'
    category_xpath='/html/body/section[4]/div/div[2]/div/article['+str(i1)+']/p[2]/a[1]'
    cmt_counter_xpath='/html/body/section[4]/div/div[2]/div/article['+str(i1)+']/p[2]/a[2]/span'
    author_name_xpath='/html/body/section[4]/div/div[2]/div/article['+str(i1)+']/p[2]/a[3]'
    #....
    tmpstr=driver.find_element(By.XPATH,title_xpath).text
    dict2["Title news"]=tmpstr
    tmpstr=driver.find_element(By.XPATH,description_xpath).text
    dict2["Description"]=tmpstr
    tmpstr=driver.find_element(By.XPATH,cmt_counter_xpath).text
    dict2["Comment Counter"]=tmpstr
    tmpstr=driver.find_element(By.XPATH,category_xpath).text
    dict2["Category"]=tmpstr
    tmpstr=driver.find_element(By.XPATH,author_name_xpath).text
    dict2["Author's name"]=tmpstr
    dict["Bài "+str(i1)]=dict2
    #...
f.write((json.dumps(dict,indent=3,separators=(', ',': '),ensure_ascii=False).encode('utf8')).decode())
f.close()







