import time
import pyautogui
import win32api
import win32con

def open_box():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 990, 990, 0, 0)
    time.sleep(0.2)
    pyautogui.press('e')


def close_box():
    pyautogui.press('esc')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -990, -990, 0, 0)


def putscrap(amount, roll):
    if(roll == 5 or roll == 10 or roll == 20):
        time.sleep(1)
        pyautogui.moveTo(716, 638)
        pyautogui.click(button='left')
        time.sleep(0.2)
        pyautogui.moveTo(911, 515)
        time.sleep(0.2)
        pyautogui.click(button='right')
        time.sleep(0.2)
    
        time.sleep(0.1)

        pyautogui.write(str(amount), interval=0.2)

        time.sleep(0.2)

        pyautogui.moveTo(1191, 499)
        time.sleep(0.2)

        if(roll == 20):
            pyautogui.dragTo(1703, 663, 0.2, button='left') #20x
        if(roll == 10):
            pyautogui.dragTo(1605, 661, 0.2, button='left') #10x
        if(roll == 5):
            pyautogui.dragTo(1503, 660, 0.2, button='left') #5x