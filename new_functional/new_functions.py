
# pip install pyautogui keyboard

import pyautogui
import keyboard
import time
import cv2 as cv
import numpy as np

def switch_to_next_window():
    # Simulate pressing Alt + Tab to switch to the next window
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

# Wait for a few seconds to give you time to focus on the initial window
# time.sleep(3)

# # Call the function to switch to the next window
# switch_to_next_window()

def screenshot():
    # Capture a screenshot
    time.sleep(3)
    screenshot = pyautogui.screenshot()

# Convert the screenshot to a numpy array
    screenshot_np = np.array(screenshot)

# Convert RGB to BGR (OpenCV uses BGR format)
    screenshot_bgr = cv.cvtColor(screenshot_np, cv.COLOR_RGB2BGR)

# Display the screenshot in a window
    cv.imshow('Screenshot', screenshot_bgr)

# Wait until a key is pressed
    cv.waitKey(0)

# Close all OpenCV windows
    cv.destroyAllWindows()