#from flask import Flask, request, send_from_directory, jsonify
#from os import error, getenv
#import os
#
#
#image = Flask(__name__)
#
#allowed_files = getenv('ALLOWED_EXTENSIONS').split(',')
#
#@image.post("/upload")
#def upload_files():
#    print(request.files)
#    return request.files
#
#
#@image.post("/upload/<filename>")
#def post_file(filename):
#    splited = filename.split('.')
#    file_extension = splited[len(splited) -1]
#    if (file_extension in allowed_files):
#        with open(f"./images/{file_extension}/{filename}", "wb") as f:
#            f.write(request.data)
#        return {"message": "Upload realizado com sucesso!"}, 201
#    else:
#        if(file_extension not in allowed_files):
#            return {"message": "Extensão não suportada"}, 415
#
#@image.get("/images/<filename>")
#def get_specific_file(filename):
#    splited = filename.split('.')
#    file_extension = splited[len(splited) -1]
#    return send_from_directory(
#      directory=f"./images/{file_extension}", 
#      path=filename, 
#      as_attachment=True
#    )
#
#@image.get("/images")
#def get_files():
#    print(os.walk('./images'))
#    return os.walk('./images')
#
#
##@app.post("/upload/<filename>")
##def post_file(filename):
##    splited = filename.split('.')
##    try:
##        if (splited[(len(splited)) -1] in getenv('ALLOWED_EXTENSIONS')):
##            with open(f"./{getenv('FILES_DIRECTORY')}/{filename}", "wb") as f:
##                f.write(request.data)
##                return {"message": "Upload realizado com sucesso!"}, 201
##    except:
##        return {"message": "Extensão não suportada"}, 415
#
#
#