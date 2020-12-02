from app import app
from config import *

from waitress import serve
serve(app, host=SERVER_URL, port=SERVER_PORT)

