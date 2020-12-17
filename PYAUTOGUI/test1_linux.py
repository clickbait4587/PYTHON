import pyautogui

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

move_mouse_relatively()