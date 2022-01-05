from flask import Flask, request, send_from_directory
from os import getenv
import os

allowed_files = getenv('ALLOWED_EXTENSIONS').split(',')
files_directory = getenv('FILES_DIRECTORY')

def upload_files():
    message = {'msg': 'Upload realizado com sucesso!'}, 201
    for file in request.files:
        filename = request.files[file].filename
        splited = filename.split('.')   
        file_extension = splited[len(splited) -1]

        if (file_extension in allowed_files):
            content = os.walk(f'{files_directory}/{file_extension}')
            for insider_file in content:
                print(filename not in insider_file[2])
                if(filename not in insider_file[2]):
                    with open(f"./{files_directory}/{file_extension}/{filename}", "wb") as f:
                        f.write(request.data)
                else:
                    message = {'msg': 'Um ou mais arquivos estão sendo adicionados repetidamente'}, 410

        if (file_extension not in allowed_files):
            message = {'msg': 'Upload apenas suporta .png, .jpg, .jpeg e .gif'}, 415
    return message


def get_files():
    after_walk = os.walk(f'../{files_directory}')
    uploaded_files = []
    for list_of_files in after_walk:
        files = (list_of_files[2])
        for file in files:
            uploaded_files.append(file)
    return {'uploaded_files': uploaded_files}

def get_specific_file(extension):
    after_walk = os.walk(f'./{files_directory}/{extension}')
    uploaded_files = []
    for list_of_files in after_walk:
        files = (list_of_files[2])
        for file in files:
            uploaded_files.append(file)
    return {f'uploaded_files_in_{extension}': uploaded_files}

def download_file(filename):
    splited = filename.split('.')
    file_extension = splited[len(splited) -1]

    return send_from_directory(
      directory=f"./{files_directory}/{file_extension}", 
      path=filename, 
      as_attachment=True
    ), 200

def downloadZip():
    file_extension = request.args.get('file_extension')
    compression_rate = request.args.get('compression_rate')

    if (int(compression_rate) < 6 or int(compression_rate) == False):
        compression_rate = 6

    os.system(f'zip -r zip/{file_extension}.zip {files_directory}/{file_extension} * -{compression_rate}')

    return send_from_directory(
        directory="./zip", 
        path=f'{file_extension}.zip', 
        as_attachment=True
    ), 200