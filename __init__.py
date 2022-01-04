from flask import Flask
from os import getenv
import os

init = Flask(__name__)

allowed_files = getenv('ALLOWED_EXTENSIONS').split(',')

def createDirectories():
    try:
        os.mkdir('images')
        print('Directory created')
    except FileExistsError:
        print('Directory already exists')

    for extension in allowed_files:
        try:
            os.mkdir(f'./images/{extension}')
            print(f'Subdirectory {extension} created')
        except FileExistsError:
            print(f'Subdirectory {extension} already exists')

    print('Inicialized successfully, all directories created.')

createDirectories()