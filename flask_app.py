from flask import Flask, request, render_template, url_for, redirect, flash, jsonify, send_file
from werkzeug.utils import secure_filename
import requests
import os
import plugs.myGDrive as myGDrive

UPLOAD_FOLDER = 'mysite/static/upload_data'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_request
def before_func():
    lst = os.listdir("/static/cloud")
    for i in lst:
        os.remove("static/cloud/"+i)

@app.route('/', methods=["GET", "POST"])
def index():
    return "hello boi its fury assist".capitalize()

@app.route('/cloud-create', methods=["GET", "POST"])
def cre():
    file = request.args.get("f")
    data = request.args.get("data")
    myGDrive.create_file(file,data)
    return " RESPONSE : 200"


@app.route('/cloud-download', methods=["GET", "POST"])
def cloud_download():
    file = request.args.get("f")
    myGDrive.download_file(file)
    return send_file("static/cloud/"+file)

@app.route('/cloud-upload', methods=('POST',"GET"))
def cloud_upload():
    files = request.files.getlist('files')
    for file in files:
        fn = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, fn))
    return 'RECEVED : 200'

@app.route('/upload', methods=('POST',"GET"))
def upload():
    files = request.files.getlist('files')
    for file in files:
        fn = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, fn))
    return 'RECEVED : 200'


if __name__ == "__main__":
    app.run()

