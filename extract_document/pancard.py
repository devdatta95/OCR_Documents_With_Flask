import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
import os.path
import re
import numpy as np
from utils.utils import *
from config import *
import logging
logger = logging.getLogger("main")

# NOTE: # If you don't have tesseract executable in your PATH, include the following:
# FOR WINDOWS
pyt.pytesseract.tesseract_cmd = TESSRACT_PATH


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    text = text.split()
    logger.debug("[INFO] Pancard Raw text: `{}` ".format(text))
    # create a list of unwanted word to remove in lower case only
    remove = ["permanent", "account", "income","tax", "number", "card", "department", "name", "father'", "father's", "father", "of", "signature",
              "govt.", "india", "card", "birth", "date", "fathers", "ante", "twat", "Number."]

    # remove all the unwanted text with
    text = [t for t in text if len(t) >= 4 and t.lower().strip() not in remove]

    return text


def get_pan_number(image_path):
    img = cv2.imread(image_path)

    # resize the image
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # convert the image to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # the following command uses the tesseract directory path to get the trained data in the config option
    text = pytesseract.image_to_string(img)

    clean_text = cleanup_text(text)

    date_regex = "^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$"
    pan_regex = r'^[a-zA-Z]{5}[0-9]{4}[a-zA-Z]$'

    pan_details = {}

    names = []

    for i in clean_text:
        if re.search(pan_regex, i):
            pan_details["Pan No: "] = i
        elif re.search(date_regex, i):
            pan_details["Birth Date: "] = i
        else:
            names.append(i)

    pan_details["Names:"] = " ".join(names)

    return pan_details
