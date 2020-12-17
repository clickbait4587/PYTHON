from selenium import webdriver
import time, random, os
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
money_one = "https://ouo.io/3d06Q"

def delay():
    time.sleep(random.randint(2,4))
print(os.getcwd ()+ '/chromedriver_linux')
driver = webdriver.Chrome(os.getcwd ()+ '/chromedriver_linux')
https = ["169.57.1.84:80", "169.57.1.84:8123", "169.57.1.85:8123", "201.91.82.155:3128", "169.57.157.146:8123", "200.17.137.40:3128", "159.255.188.134:41258", "150.138.253.70:808", "169.57.157.148:8123", "158.255.215.50:16993", "169.57.157.148:25", "159.8.114.37:8123", "150.138.253.73:808", "119.81.189.194:8123", "183.220.145.3:80"]

def set_proxy():
    PROXY = https[5]
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,

        "proxyType":"MANUAL",
        "class":"org.openqa.selenium.Proxy",
       "autodetect":False

    }
set_proxy()
driver.maximize_window()

def wait_for_btn():
    print("Bout to click...")
    element = WebDriverWait(driver, 20).until(

    EC.element_to_be_clickable((By.ID, "btn-main")))

    element.click()

def get_money():
    print("Getting The Money...")
    driver.get(money_one)

    delay()
    wait_for_btn()
    delay()
    wait_for_btn()
    #driver.close()

for i in range(5):
    get_money()