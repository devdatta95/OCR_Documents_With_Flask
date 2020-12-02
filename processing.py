from extract_document.bank_cheque import *
from extract_document.pancard import *
from extract_document.face import *
from extract_document.driving_licence import *
from extract_document.adhar_card import *
from utils.utils import *
import cv2
import logging
logger = logging.getLogger("main")



def text_detection(img_path, doc_type):
    """

    :param img_path: input image_path for processing
    :param doc_type: document type
    :return: image with extracted text
    """
    img = cv2.imread(img_path)

    # document is bank_cheque
    if doc_type == "Bank_Cheque":

        cheque_details = {}

        # get details from the image
        cheque_details["ACC_No."] = ensemble_acc_output(img_path)
        cheque_details["IFSC"] = ensemble_ifsc_output(img_path)
        cheque_details["MICR"] = get_micrcode(img_path)

        logger.debug("[INFO] Cheque details extracted: {}".format(cheque_details))

        return img, cheque_details

    elif doc_type == "Pancard":

        # get details from the image
        pan_details = get_pan_number(img_path)

        # detect face in the document
        isface, image = detect_faces(img_path)

        if isface:
            pan_details["Face_Found"] = "True"
        else:
            pan_details["Face_Found"] = "False"

        logger.debug("[INFO] Pancard Clean Text Extracted: {}".format(pan_details))

        return image, pan_details


    elif doc_type == "Driving_Licence":

        # recognize raw text first
        raw_text = recognise_text(img_path)
        logger.debug("[INFO] Driving Licence Raw Text `{}`".format(raw_text))

        # extract labels from the recognised text according to the image_type
        license_details = {idx: text for idx, text in enumerate(raw_text)}
        license_details = get_licence_text(license_details)

        # detect face in the document
        isface, image = detect_faces(img_path)

        if isface:
            license_details["Face_Found"] = "True"
        else:
            license_details["Face_Found"] = "False"

        logger.debug("[INFO] Driving Licence Clean Text Extracted: {}".format(license_details))

        return image, license_details

    elif doc_type == "Aadhar_Card":

        # recognize raw text first
        raw_text = recognise_text(img_path)
        logger.debug("[INFO] Aadhar Card Raw Text `{}`".format(raw_text))

        # extract labels from the recognised text according to the image_type
        aadhar_details = get_aadhar_text(raw_text)

        # detect face in the document
        isface, image = detect_faces(img_path)

        if isface:
            aadhar_details["Face_Found"] = "True"
        else:
            aadhar_details["Face_Found"] = "False"

        logger.debug("[INFO] Aadhar Card  Clean Text Extracted: {}".format(aadhar_details))

        return image, aadhar_details

    # if the document
    elif doc_type == "Others":

        # extract all the text
        others_details = simple_text_extraction(img_path)

        others_details = clean_text(others_details)
        others_details = [  i for i in others_details.split() if len(str(i)) >= 4 ]

        # detect face in the document
        isface, image = detect_faces(img_path)

        final_details = dict()
        final_details["Extracted Data"] = others_details

        if isface:
            final_details["Face"] = "Face Found"
        else:
            final_details["Face"] = "Face Not Found"

        logger.debug("[INFO] Other Document Clean Text Extracted: {}".format(final_details))


        return image, final_details


    else:
        logger.debug("[INFO] No document present...")
        return img, "No text found"











