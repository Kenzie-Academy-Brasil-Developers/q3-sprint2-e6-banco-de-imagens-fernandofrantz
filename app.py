from flask import Flask, request, send_from_directory
from os import getenv

app = Flask(__name__)

@app.post("/upload/<filename>")
def post_file(filename):
    splited = filename.split('.')
    if(filename):
        print(request.files)
    if (splited[(len(splited)) -1] == 'png' or 
        splited[(len(splited)) -1] == 'jpg' or 
        splited[(len(splited)) -1] == 'gif'):
        with open(f"./images/{filename}", "wb") as f:
            f.write(request.data)
            return {"message": "Upload realizado com sucesso!"}, 201
    return {"message": "Extensão não suportada"}, 415


