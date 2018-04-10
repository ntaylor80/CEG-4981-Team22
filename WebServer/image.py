import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64
from math import sqrt

with open("test2.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())

# BGR [low] [high] values OpenCV reverses color order
# boundaries = [
#     ([173, 63, 0], [255, 179, 135]),  # Blue mask lower/upper
#     ([0, 69, 200], [0, 147, 255])  # Orange mask Lower/Upper
# ]

boundaries = [
    ([160, 90, 15],[255, 255, 120]),  # Blue mask lower/upper
    ([50, 100, 200], [180, 200, 255])  # Orange mask Lower/Upper
]

lower_blue = np.array([35, 63, 0])
upper_blue = np.array([255, 179, 135])

def analyze_image(image):


    pil_img = Image.open(BytesIO(base64.b64decode(image))).convert('RGB')

    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2GRAY)

    img_color = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    #countStars(img)

    result = list()
    i = 0
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(img_color, lower, upper)
        cv2.imwrite("mask{}.png".format(i),mask)
        # cv2.imshow("test",mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        i+= 1
        result.append(countStars(mask))

    return result


def countStars(image):
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    img, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    starCount = 0
    divMaxSize = 0.175
    divMinSize = 0.125
    areas = list()
    for contour in contours:

        cnt = contour
        area = cv2.contourArea(contour)
        if area == 0:
            continue
        arcLen = cv2.arcLength(cnt, True)

        prop = sqrt(area) / arcLen

        if (prop < divMaxSize and prop > divMinSize):
            # print("I'm a star")
            areas.append(area)

    if areas:
        max_area = max(areas)
        for area in areas:
            error = np.abs((max_area - area) / max_area) * 100
            if error < 10:
                starCount += 1
        print("stars ",starCount)

    return starCount



