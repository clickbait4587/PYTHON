import pyautogui, time
import pytesseract, os
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pyautogui.PAUSE = 1 #1s pause after each function
pyautogui.FAILSAFE = True #Enable Failsafe mode

#CONTROLLING MOUSE MOVEMENT

resolution = pyautogui.size()
width, height = resolution

print(f"{width} x {height}")

#MOVING THE CURSOR
def move_mouse_absolutely():

    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

def move_mouse_relatively():
    print("Moving mouse relative;y")
    for i in range(10):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

def get_post():
    while True:
        print(pyautogui.position())

def click_mouse(x,y):
    pyautogui.click(x,y)

def goto(x,y):
    pyautogui.moveTo(x,y, duration=0.35)
def click_here(img):
    print(pyautogui.locateOnScreen(img))
def main():
    goto(337,89)
    #pyautogui.hotkey('ctrl', '')
    pyautogui.keyDown('ctrl')
    pyautogui.click()
    pyautogui.keyUp('ctrl')
    #click_mouse(416, 64)
    #time.sleep(2)
    #pyautogui.typewrite("clicktonics.com")
    #pyautogui.typewrite('enter')

def img_to_txt():
    img = Image.open('texthand.PNG')
    text = pytesseract.image_to_string(img)
    print(text)
img_to_txt()
