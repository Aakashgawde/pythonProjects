# Automated text messaging


# Import relevant modules
import time
import pyautogui


def SendMessage():
    time.sleep(10)
    text  = open('message.txt')

    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

SendMessage()