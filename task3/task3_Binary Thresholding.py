"""
NAME: SAMUEL OSEI BOAKYE
ID:10953117
COURSE: COMPUTER VISION
"""
import cv2
import numpy as np

# Single pixel 
pixel = np.array([[180]], dtype=np.uint8)
threshold_value = 150
_, binary = cv2.threshold(pixel, threshold_value, 255, cv2.THRESH_BINARY)

print(f"Original: {pixel[0][0]}")
print(f"Thresholded: {binary[0][0]}") 

# The codes Will output 255
