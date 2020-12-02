# import the necessary packages
from os import path


# flask ip
SERVER_URL = "0.0.0.0"

# flask port
SERVER_PORT = 8090

# upload folders
IMAGE_UPLOADS = "uploads/"
TEMP_IMAGES = "uploads/Temp"

FACE_HAARCASCADE = "models/haarcascade_frontalface_default.xml"

TESSRACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
LOGFILE = "logs/main.log"

# HEROKU_TESRACT_PATH = "/app/.apt/usr/bin/tesseract"