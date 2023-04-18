import pytesseract
import cv2
import numpy as np
import pyautogui
import re

from PIL import Image
import pytesseract


def getWheelCircle(contrast, brightness):
    x, y, width, height = 630, 220, 620, 390
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

    M = cv2.getRotationMatrix2D(center, -90, 1.0)
    img  = cv2.warpAffine(img, M, (w, h))

    img = cv2.addWeighted( img, contrast, img, 0, brightness)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite('tmp.png', img)
    return img


def percentage(part, whole):
    return (part * whole) / 100.0

def extract_numbers(s):
    digits = re.findall(r'\d+', s)
    return int(''.join(digits))

def getCount(img):

    # Define the lower and upper boundaries for each color
    red_lower = np.array([0, 0, 150])
    red_upper = np.array([50, 50, 255])
    pink_lower = np.array([150, 50, 150])
    pink_upper = np.array([255, 150, 255])
    blue_lower = np.array([150, 100, 0])
    blue_upper = np.array([255, 225, 50])

    # Threshold the image to obtain only the pixels that are within the color range
    red_mask = cv2.inRange(img, red_lower, red_upper)
    pink_mask = cv2.inRange(img, pink_lower, pink_upper)
    blue_mask = cv2.inRange(img, blue_lower, blue_upper)

    # Count the number of pixels in each color range
    red_count = cv2.countNonZero(red_mask)
    pink_count = cv2.countNonZero(pink_mask)
    blue_count = cv2.countNonZero(blue_mask)

    # Print the number of pixels found for each color
    print(f"Red count: {red_count}")
    print(f"Pink count: {pink_count}")
    print(f"Blue count: {blue_count}")

def get_color_name(rgb):
    colors = {
        "blue": (69, 104, 157),
        "yellow": (162, 149, 74),
        "green": (36,124, 12),
        "yellow": (156,139,68),
        "yellow": (149, 129, 112),
        "yellow": (145, 110, 2),
        "green": (63, 102, 43),
        "blue": (84, 78, 91),
        "yellow": (160, 146, 132),
        "green": (98, 144, 52),
        "yellow": (173, 151, 85),
        "red": (178, 90, 41),
        "pink": (134, 76, 130)
    }
    min_distance = float("inf")
    closest_color = None
    for color, value in colors.items():
        distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    return closest_color
