from flask import Flask, request, render_template, url_for, redirect, flash, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import plugs.myGDrive as myGDrive
from plugs.service_management import *
import tempfile
from io import BytesIO

UPLOAD_FOLDER = 'static\\temp\\'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_request
def before_func():
    clear_cloud()
    clear_temp()

@app.route('/', methods=["GET", "POST"])
def index():
    return "<----- the fury assist node PCS -----> "

@app.route("/api/cloud-create", methods=('POST',"GET"))
def create_file():
    name = request.args.get("name")
    content = request.args.get("content")
    myGDrive.create_file(name=name,data=content)
    return "200"

@app.route("/api/cloud-upload", methods=('POST',"GET"))
def upload_file():
    data = []
    files = request.files.getlist('files')
    for file in files:
        fn = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],fn))
        d = myGDrive.upload_file(os.path.join(app.config['UPLOAD_FOLDER'],fn))
        data.append({fn:d})
        clear_temp()
    return jsonify(data)

@app.route("/api/cloud-send")
def send_file_cloud():
    file = request.args.get("file")
    id = request.args.get("id")
    if not id : id = None
    title = myGDrive.download_file(file,id=id)
    clear_cloud()
    return send_file("static/cloud/"+title)
    

@app.route("/api/cloud-list")
def list_file():

    data = myGDrive.get_file_list()
    return jsonify(data)


app.run(port=2004,debug=True)