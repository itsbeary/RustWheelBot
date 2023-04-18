import cv2
import numpy as np
from util import *

getWheelCircle()

# Load image and convert to grayscale
img = cv2.imread('tmp.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Apply Hough transform to find circles
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Get center of circle
center = int(circles[0][0][0]), int(circles[0][0][1])

# Get radius of circle
radius = int(circles[0][0][2])

# Define colors and their corresponding multipliers
colors = {1: 'red', 2: 'pink', 4: 'blue', 6: 'green', 11: 'yellow'}
multipliers = {20: 'red', 10: 'pink', 5: 'blue', 3: 'green', 1: 'yellow'}

# Set angle range for strips on the left side of the wheel
start_angle = -67
end_angle = 68

# Define dictionary to store strip colors and their counts
strip_colors = {'red': 0, 'pink': 0, 'blue': 0, 'green': 0, 'yellow': 0}

# Loop through each strip and count its color
for i in range(24):
    # Get start and end angles for current strip
    strip_start_angle = i * 15 - 7.5
    strip_end_angle = strip_start_angle + 26

    # Only count strips on the left side of the wheel
    if strip_end_angle < end_angle:
        continue
    if strip_start_angle > start_angle:
        break

    # Get the strip color
    strip_center = int(center[0] + radius * np.cos(strip_start_angle * np.pi / 180)), int(center[1] + radius * np.sin(strip_start_angle * np.pi / 180))
    strip_color = colors.get(img[strip_center[1], strip_center[0]], None)

    # Get the strip multiplier
    multiplier_center = int(center[0] + radius * np.cos((strip_start_angle + strip_end_angle) / 2 * np.pi / 180)), int(center[1] + radius * np.sin((strip_start_angle + strip_end_angle) / 2 * np.pi / 180))
    multiplier = multipliers.get(img[multiplier_center[1], multiplier_center[0]], None)

    # If the strip color and multiplier are valid, update the counts
    if strip_color and multiplier:
        if strip_color == multiplier:
            strip_colors[strip_color] += 1

# Print out strip color counts
print(strip_colors)