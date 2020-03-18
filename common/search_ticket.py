#coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import date,timedelta
from base.common_fun import id, xpath,js_remove_attr_readonly,return_driver,date_n,read_excel,log_config
import logging

def search_ticket():
    excle_data = read_excel("../testData/testData.xlsx",0)
    driver = return_driver()
    driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
    #等待元素加载，10S，过后超时
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(3)
    id("notice01").send_keys(excle_data[0][0])
    time.sleep(3)
    id("notice08").send_keys(excle_data[0][1])
    time.sleep(3)
    #由于时间插件的只读属性，需要通过JS脚本更改readonly属性
    # JS = "document.getElementById('dateobj').removeAttribute('readonly')"
    # driver.execute_script("document.getElementById('dateObj').removeAttribute('readonly')")
    js_remove_attr_readonly("dateObj")
    #格式化一个传入时间
    leave_date = date_n(1)
    #清除默认传入时间
    id("dateObj").clear()
    id("dateObj").send_keys(leave_date)
    action = ActionChains(driver)
    action.move_by_offset(0,0).click().perform()
    id("searchbtn").click()
