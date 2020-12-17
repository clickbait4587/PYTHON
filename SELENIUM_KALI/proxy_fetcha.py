from selenium import webdriver
import time
import json
import urllib
import sys
import ffmpy
import pydub
import speech_recognition as sr
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

driver = webdriver.Chrome('./chromedriver.exe')

def delay ():
    time.sleep(random.randint(2,4))


def save_prox(proxy_list):
    https = []
    with open('./https.json') as ps:
        ps = json.load(ps)['https']
        for i in proxy_list:
            ps.append(i)
        with open('./https.json', 'w') as ps2:
            json.dump({"https": ps}, ps2)
            print('Done')
    
def get_prox():
    driver.find_element_by_id('protocol_https').click()
    delay()
    driver.find_element_by_class_name('fa-sync').click()

    tables = driver.find_elements_by_css_selector('tr td a')
    https = []
    for table in tables:
        https.append(table.text)
    save_prox(https)
    
class Play:
    def __init__(self, arg1=None):
        self.arg1 = arg1
    delay()
    def get_aud(self):

        frames = driver.find_elements_by_tag_name('iframe')
        #driver.switch_to.frame(driver.find_element_by_name("c-sxxupvniali4"))
        #aud_btn = driver.find_element_by_id('recaptcha-audio-button')
        #aud_btn.click()
        #captcha_cont = driver.find_element_by_id('rc-imageselect')

        driver.switch_to.frame(frames[-1])
        aud_btn = driver.find_element_by_id('recaptcha-audio-button')
        aud_btn.click()
        delay()
        for button in driver.find_elements_by_tag_name('button'):
            if button.text == "PLAY":
                print(button.text)
                button.click()
        delay()
        src = driver.find_element_by_id('audio-source').get_attribute('src')
        #print(f"Audio: {src}")
        #Download Audio
        delay()
        urllib.request.urlretrieve(src,os.getcwd()+"\\audio.mp3")
    def mp3_to_wav(self):
        print("Mp3 to wav")
        #sound = pydub.AudioSegment.from_mp3(os.getcwd()+"\\audio.mp3")
        try:
            sound = pydub.AudioSegment.from_mp3(os.getcwd()+"\\audio.mp3")
            print(sound)
            sound.export(os.getcwd()+"\\audio.wav", format="wav")
            samp_aud = sr.AudioFile(os.getcwd() + "\\audio.wav")
            
            #Aud to text
            r = sr.Recognizer()
            with samp_aud as source:
                audio = r.record(source)
            
            key=r.recognize_google(audio)
            #print("[INFO] Recaptcha Passcode: %s"%key)
            #send results
            driver.find_element_by_id("audio-response").send_keys(key.lower())
            
            driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
            delay()
            
        except:
            driver.find_element_by_id("audio-response").send_keys("key.lower()")
            
            driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
            e = sys.exc_info()
            print(e)
    

    

    
    #print(aud_btn)
play = Play()

def main():
    
    #driver.maximize_window()
    proxy_site = "http://proxydb.net/"
    driver.get(proxy_site)
    get_prox()
    delay()
    driver.find_element_by_css_selector('button[data-sitekey="6LdiWTYUAAAAALwxWXVjqSgJY0miidTeuDcAvbm1"]').click()
    #play()
    play.get_aud()
    play.mp3_to_wav()
    if driver.find_element_by_id("audio-response"):
        while not driver.find_element_by_id("audio-response").text:
            print("No text")
            #aud_btn = driver.find_element_by_id('recaptcha-audio-button')
            #aud_btn.click()
            #delay()
            for button in driver.find_elements_by_tag_name('button'):
                if button.text == "PLAY":
                    print(button.text)
                    button.click()
            delay()
            src = driver.find_element_by_id('audio-source').get_attribute('src')
            #print(f"Audio: {src}")
            #Download Audio
            delay()
            urllib.request.urlretrieve(src,os.getcwd()+"\\audio.mp3")
            play.mp3_to_wav()
        else:
            print("There is text")
    print('done')
    #get the mp3 audio file
    #src = driver.find_element_by_id("audio-source").get_attribute("src")
    #print("[INFO] Audio src: %s"%src)
    #download the mp3 audio file from the source
    #urllib.request.urlretrieve(src, os.getcwd()+"\\sample.mp3")
    
main()

