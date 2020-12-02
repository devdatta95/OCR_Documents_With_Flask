"""
@author: devdatta supnekar
@topic: ocr on documents
@created_on: 29/11/2020
@last_updated:
@updated_by

"""
# imports
from flask import Flask, flash, Response, redirect, url_for, render_template, request
import pandas as pd
from config import *
import numpy as np
import imutils
import time
import cv2
import os
import datetime
from werkzeug.utils import secure_filename
from processing import *
from utils.log import log_setup

# initialize all golbal variables
outputFrame = None
imageFrame = None

logger = log_setup("main", LOGFILE)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


############################## FILES UPLOAD #################################

# route for home page
@app.route("/")
def index():
    return render_template("index.html")


# route to upload files
@app.route("/upload", methods=['GET', 'POST'])
def upload():

    # if request.method == "POST":
    if "photo" in request.files:
        # get image file from request
        file = request.files["photo"]
        # get document type from request
        doc_type = request.form["type"]
        logger.debug("[INFO] Request received for `{}`...".format(doc_type))

        timeStamp = time.strftime('%d-%m-%Y_%H-%M-%S')

        # if the doc_type folder doesn't alredy exist, create it
        if not os.path.exists(IMAGE_UPLOADS + doc_type):
            os.mkdir(IMAGE_UPLOADS + doc_type)
            # directory for saving faces in the id cards
            os.mkdir(IMAGE_UPLOADS + doc_type + "/" + "Faces")

        # sequre the namee
        img_name = secure_filename(file.filename)


        # setting filename that is being received to current time stamp with its directory
        save_path = IMAGE_UPLOADS + doc_type + "/" + img_name
        file.save(save_path)
        logger.debug("[INFO] Document image file uploaded successfully: `{}` ".format(save_path))

        logger.debug("[INFO] Processing image file...")
        # image = cv2.imread(save_path)
        # print(image)

        # detect faces in the frame and detect the emotion
        global imageFrame

        # Note: use your function here
        imageFrame, details = text_detection(save_path, doc_type)


        
        # savepath = os.path.join(TEMP_IMAGES, "temp_{}_{}".format(timeStamp, ".jpg"))
        # cv2.imwrite(savepath, imageFrame)
        # logger.debug("[INFO] Saving Document Copy...")

        logger.debug("[INFO] Request Completed for `{}` ".format(doc_type))
        logger.debug("######################################################################################")
        return render_template("image.html", details=details)


########################### IMAGE PROCESSING ####################################


# function to encode image files and send to client
def GetImage():
    global imageFrame

    # encode the frame in JPEG format
    (flag, img) = cv2.imencode(".png", imageFrame)

    while True:
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n')


# route to display image output
@app.route("/display_image")
def display_image():
    return Response(GetImage(), mimetype="multipart/x-mixed-replace; boundary=frame")



if __name__ == "__main__":
    app.run(host=SERVER_URL, port=SERVER_PORT, debug=True)
