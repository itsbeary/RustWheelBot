import pytesseract
import cv2
import numpy as np
import pyautogui
import re
from scipy import ndimage
from PIL import Image
import pytesseract
import imutils
from scipy.spatial import KDTree
from webcolors import css3_hex_to_names, hex_to_rgb

    


def getScrap():
    x, y, width, height = 705, 634, 80, 40

    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Beary\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(screenshot)

    return text.replace("x", "").replace(',', "")

def getWheelCircle():
    x, y, width, height = 630, 230, 620, 390
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    screenshot = np.array(screenshot)
    center = (screenshot.shape[1]//2, screenshot.shape[0]//2) # center of the image
    radius = 200

    mask = np.zeros(screenshot.shape[:2], dtype=np.uint8)
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    cropped_img = cv2.bitwise_and(screenshot, screenshot, mask=mask)

    h, w = cropped_img.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), -40, 1)
    rotated_img = cv2.warpAffine(cropped_img, M, (w, h))

    height, width = rotated_img.shape[:2]
    img = rotated_img[:, :width//2]

    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #cv2.imwrite("wheel-images/wheel_current.png", img)

def percentage(part, whole):
    return (part * whole) / 100.0

def extract_numbers(s):
    digits = re.findall(r'\d+', s)
    return int(''.join(digits))

def convert_rgb_to_names(rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []    
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)   
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'