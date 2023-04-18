import pyautogui
import time
from PIL import Image
from util import *
from scrap import *
import numpy as np
from jpype import *

startJVM("-ea", classpath=["RustWheel.jar"])
wheelClass = JClass("net.kealands.Main")

wheel = getWheelCircle(1, 0)

wheelClass.start()
print("red: ", wheelClass.getRed(), " blue: ", wheelClass.getBlue(), " pink: ", wheelClass.getPink())

cv2.imshow("image", wheel)
cv2.waitKey(0)
cv2.destroyAllWindows()