import cv2
import numpy as np
import random

images = ["Indexation_placeholder", "Color-Me-Impressed/gettyimages-1401562475-612x612.jpg", "Color-Me-Impressed/istockphoto-517188688-612x612.jpg", "Color-Me-Impressed/pexels-souvenirpixels-417074.jpg", "Color-Me-Impressed/UCBerkeleyCampus-scaled.jpg", "Color-Me-Impressed/kremlin-wall-night-moscow-590.avif"]
while True:                 
    image_to_be_read = input("Hello, welcome to my OpenCV color detection software. Would you like to analyze a specfic image or a random one? (specific | random): ").lower()        
    if image_to_be_read == "random":
        image_to_be_read = images[random.randint(0, 4)]
        break
    elif image_to_be_read == "specific":
        image_index = input("Which Image would you like?\n1. New York Street\n2. Grassy Mountain Side\n3. Mountain Side Lake\n4. The number ONE public school\n5. Moscow Night\n(Input Number): ")
        if image_index.isdigit() == False or int(image_index) not in range (1, 6):
            print(type(image_index))
            print(image_index.isalnum())
            print("Please enter an integer on the list!")
        else:
            image_to_be_read = images[int(image_index)]
            break
    else:
        print("Check your spelling!")

image = cv2.imread(image_to_be_read)
if image is None:
    raise ValueError("Image not found or not able to load.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

red_lower1 = np.array([0, 100, 100])
red_upper1 = np.array([10, 255, 255])
red_lower2 = np.array([160, 100, 100])
red_upper2 = np.array([179, 255, 255])

white_lower = np.array([0, 0, 200])
white_upper = np.array([180, 50, 255])

blue_lower = np.array([85, 100, 50])
blue_upper = np.array([130, 255, 255])

green_lower = np.array([35, 50, 50])
green_upper = np.array([85, 255, 255])

mask_red1 = cv2.inRange(hsv, red_lower1, red_upper1)
mask_red2 = cv2.inRange(hsv, red_lower2, red_upper2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)
mask_white = cv2.inRange(hsv, white_lower, white_upper)
mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
mask_green = cv2.inRange(hsv, green_lower, green_upper)

red_area = cv2.bitwise_and(image, image, mask=mask_red)
white_area = cv2.bitwise_and(image, image, mask=mask_white)
blue_area = cv2.bitwise_and(image, image, mask=mask_blue)
green_area = cv2.bitwise_and(image, image, mask=mask_green)

cv2.imshow('Original Image', image)
cv2.imshow('Red Area', red_area)
cv2.imshow('White Area', white_area)
cv2.imshow('Blue Area', blue_area)
cv2.imshow('Green Area', green_area)
cv2.waitKey(0)
cv2.destroyAllWindows()