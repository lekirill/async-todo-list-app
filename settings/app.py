import os

HOST = os.getenv('HOST') or '0.0.0.0'
PORT = os.getenv('PORT') or 8080
DEBUG = os.getenv('DEBUG') or True
NUM_OF_WORKERS = os.getenv('NUM_OF_WORKERS') or 1
