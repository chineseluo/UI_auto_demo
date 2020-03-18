#coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import date,timedelta
from base.common_fun import id, xpath,js_remove_attr_readonly,return_driver,log_config
from common.search_ticket import search_ticket
log_config("Begin Search Test")
search_ticket()
log_config("End Search test")
driver = return_driver()
log_config("Click Start")
xpath("//*[starts-with(@id,'tbody-01-G21950')]/div[1]/div[6]/div[3]/a").click()
log_config("input Name")
xpath("//*[@id='pasglistdiv']/div/ul/li[2]/input").send_keys("chineseluo")
time.sleep(2)
driver.quit()

