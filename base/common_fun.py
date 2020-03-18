#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time
import xlrd
import logging
from datetime import date,timedelta
driver = webdriver.Chrome("D:/chromedriver/chromedriver_win32_75/chromedriver.exe")
def return_driver():
    return driver

#代码优化部分
def id(element):
    return driver.find_element_by_id(element)

def css(element):
    return driver.find_element_by_css_selector(element)

def js_remove_attr_readonly(element):
    print(type(element))
    print("document.getElementById("+element+").removeAttribute('readonly')")
    print(type("document.getElementById("+element+").removeAttribute('readonly')"))
    driver.execute_script("document.getElementById("+"'"+element+"'"+").removeAttribute('readonly')")

def xpath(element):
    return driver.find_element_by_xpath(element)

def date_n(n):
    return str((date.today()+timedelta(days=+int(n))).strftime("%Y-%m-%d"))

def read_excel(filename,index):
    testDataPath = filename
    xls = xlrd.open_workbook(testDataPath)
    sheet = xls.sheet_by_index(index)
    data_dic = {}
    for i in range(sheet.ncols):
        data = []
        for j in range(sheet.nrows):
            if j == 0:
                continue
            else:
                data.append(sheet.row_values(j)[i])
        data_dic[i] = data
        print(data_dic)
    return data_dic

def log_config(str):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"
    logging.basicConfig(filename="test_log.log",level=logging.DEBUG,format=LOG_FORMAT,datefmt=DATE_FORMAT)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)


