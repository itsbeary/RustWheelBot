import pyautogui
import time
from PIL import Image
from util import *
from scrap import *
import numpy as np
from webcolors import rgb_to_name

# amount = round(percentage(1, extract_numbers(getScrap())))

wheel_points = [(289, 50), (260, 68), (232, 88), (208, 112), (196, 142), (193, 179), (192, 212), (202, 243), (217, 272), (242, 301), (272, 317), (305, 329)]




def printColours():
    img = Image.fromarray(getWheelCircle())
    for point in wheel_points:
        color = img.getpixel(point)
        print(convert_rgb_to_names(color))
printColours()
