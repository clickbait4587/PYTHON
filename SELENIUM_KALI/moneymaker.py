from selenium import webdriver
import time, random
money = "http://gestyy.com/etrboZ"
def delay30():
    time.sleep(10)
def delay():
    
    time.sleep(random.randint(2,4))

https = ["169.57.1.84:80",
 "169.57.1.84:8123",
  "169.57.1.85:8123",
   "201.91.82.155:3128",
    "169.57.157.146:8123",
     "200.17.137.40:3128",
      "159.255.188.134:41258",
       "150.138.253.70:808",
        "169.57.157.148:8123",
         "158.255.215.50:16993",
          "169.57.157.148:25",
           "159.8.114.37:8123",
            "150.138.253.73:808",
             "119.81.189.194:8123",
              "183.220.145.3:80"]
#def set_proxy(i):
#    print(https[i])
#    webdriver.DesiredCapabilities.CHROME['proxy']={
#        "httpProxy":https[i],
#        "ftpProxy":https[i],
#        "sslProxy":https[i],
#
#        "proxyType":"MANUAL",
#
#    }
#
ouo_scrap = "https://ouo.io/WpsICO"
won_scrap = "https://won.pe/fSDXZ"
##set_proxy(5)
##driver = webdriver.Firefox(executable_path='geckodriver.exe')
#driver= webdriver.Chrome('./chromedriver.exe')
#driver.maximize_window()

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import json
def save_prox(proxy_list):
    https = []
    with open('./https.json') as ps:
        ps = json.load(ps)['https']
        for i in proxy_list:
            ps.append(i)
        with open('./https.json', 'w') as ps2:
            json.dump({"https": ps}, ps2)
            print('Done')
def make_request():
    req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    proxies = req_proxy.get_proxy_list() #this will create proxy list
    ls = []
    for prox in proxies:
        ls.append(prox.get_address())
    save_prox(ls)
def get_proxy():
    with open('./https.json') as ps:
        ps = json.load(ps)['https']
    return ps

ps = get_proxy()

def save_working(proxy):
    with open('./working.json') as wk:
        wk = json.load(wk)['https']
        wk.append(proxy)
        wk2 = list(set(wk))
    with open('./working.json', 'w') as wk3:
        print(wk2)
        json.dump({"https": wk2}, wk3)
        print('DONE')
    #print(wk2)
#def prox():
#    return ps[random.randint(0, len(ps)-1)]
PROXY = next(iter(ps))

def set_proxy():

    print(PROXY)
    webdriver.DesiredCapabilities.FIREFOX['proxy']={
       "httpProxy": PROXY,
       "ftpProxy": PROXY,
        "sslProxy": PROXY,

        "proxyType":"MANUAL",

    }

def getter(driver):
    
    driver.maximize_window()
    driver.get(won_scrap)
    


def main():
    set_proxy()
    #driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver= webdriver.Chrome('./chromedriver.exe')
    getter(driver)
    delay()
    getter(driver)
    delay()

    driver.find_element_by_id('robot_button').click()

    def alert_closer():
        import pyautogui, time
        pyautogui.click(414, 82)
    delay30()
    alert_closer()
    delay()

    from selenium.webdriver.common.by import By

    from selenium.webdriver.support.ui import WebDriverWait

    from selenium.webdriver.support import expected_conditions as EC

    #element = WebDriverWait(driver, 20).until(
    #
    #EC.element_to_be_clickable((By.ID, "btn-main")))
    #
    #element.click();
    #
    #delay()
    #element = WebDriverWait(driver, 20).until(
    #
    #EC.element_to_be_clickable((By.ID, "btn-main")))
    #
    #element.click();
    def skip(driver):
        print("SKIPPING..")
        delay()
        skip_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "skip_button"))
        )
        skip_btn.click()
    for i in range(2):
        delay()
        skip(driver)

    save_prox(PROXY)
    

#for i in range(5):
#    try:
#        delay30()
#        main()
#    except:
#        main()
#print("DONE")

main()


