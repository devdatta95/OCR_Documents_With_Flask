import cv2
import pytesseract as pyt
import re
from ctpn.demo_pb import get_coords
from config import *
import logging
logger = logging.getLogger("main")


# NOTE: # If you don't have tesseract executable in your PATH, include the following:
# FOR WINDOWS
pyt.pytesseract.tesseract_cmd = TESSRACT_PATH


# function to remove noise and unnecessary characters from string
def clean_text(text):
    if text != ' ' or text != '  ' or text != '':
        text = re.sub('[^A-Za-z0-9-/,.() ]+', '', text)
        text = text.strip()
        text = re.sub(r'\s{2,}', ' ', text)

    return text


def simple_text_extraction(image_path):
    img = cv2.imread(image_path)
    # resize the image
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # convert the image to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # the following command uses the tesseract directory path to get the trained data in the config option
    text = pyt.image_to_string(img)
    return text


# function to recognise text from image
def recognise_text(image_path):
    # read image and convert to grayscale
    image = cv2.imread(image_path, 0)

    # get coordinates of text using ctpn
    coordinates = get_coords(image_path)

    detected_text = []

    # sorting coordinates from top to bottom
    coordinates = sorted(coordinates, key=lambda coords: coords[1])

    # looping through all the text boxes
    for coords in coordinates:
        # x, y, width, height of the text box
        x, y, w, h = coords

        # cropping image based on the coordinates
        temp = image[y:h, x:w]

        # binarizing image
        _, thresh = cv2.threshold(temp, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # padding the image with 10 pixels for better prediction with tesseract
        thresh = cv2.copyMakeBorder(thresh, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        # get text from the image, lang = english + hindi + marathi, config = use lstm for prediction
        text = pyt.image_to_string(thresh, lang="eng+hin+mar", config=('--oem 1 --psm 3'))

        # clean text and remove noise
        text = clean_text(text)

        # ignore text if the length of text is less than 3
        if len(text) < 3:
            continue
        detected_text.append(text)

    # return detected text
    return detected_text
