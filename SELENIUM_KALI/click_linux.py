from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

https = ["169.57.1.84:80", "169.57.1.84:8123", "169.57.1.85:8123", "201.91.82.155:3128", "169.57.157.146:8123", "200.17.137.40:3128", "159.255.188.134:41258", "150.138.253.70:808", "169.57.157.148:8123", "158.255.215.50:16993", "169.57.157.148:25", "159.8.114.37:8123", "150.138.253.73:808", "119.81.189.194:8123", "183.220.145.3:80"]

def delay():
    time.sleep(random.randint(2,4))
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


#req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
#proxies = req_proxy.get_proxy_list() #this will create proxy list
#sa = []
#for proxy in proxies:
#    proxy
#    if proxy.country == "United States": sa.append(proxy)
##    sa.append(proxy)
##PROXY = "85.209.149.88:8085" 
#PROXY = sa[2].get_address()
#
PROXY = https[5]
##print(PROXY)
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
   "autodetect":False
    
}
driver = webdriver.Chrome('./chromedriver_linux')
driver.maximize_window()

driver.get("https://clicktonics.com")
delay()
#driver.find_element_by_css_selector('a[title="Make Money Online Reading Emails"]').click()

while False:
    time.sleep(random.randint(5,10))
    driver.refresh()
title="ClickTonics | It's part of the package"

if driver.title != title:
    print("Quiting")
    delay()
    driver.close()