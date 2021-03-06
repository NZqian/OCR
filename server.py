from flask import Flask, request, redirect, render_template, url_for, send_file, send_from_directory
import pandas as pd
import os

import Jpeg2Excel

allowedTypes = ['jpg', 'jpeg']

class NameException(Exception):
    pass
class SuffixException(Exception):
    pass

app = Flask(__name__)

def filenameCheck(filename, allowedTypes):
    if filename == '' or (filename.split('.')[-1] not in allowedTypes):
        raise SuffixException

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        f = request.files["file"]

        #try:
        #    filenameCheck(f.filename, allowedTypes)
        #except SuffixException:
        #    return redirect(url_for('fail_suffix'))
        #else:   
        save_path = "./"
        path = os.path.join(save_path,f.filename)
        f.save(path)
        print(f.filename)
        Jpeg2Excel.main(path)
        return redirect(url_for('success'))

    return render_template("submit.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/fail')
def fail():
    return render_template("fail.html")

@app.route('/fail_suffix')
def fail_suffix():
    return render_template("fail_suffix.html")

@app.route('/download/<filename>', methods=['Get'])
def download_file(filename):
    directory = "/home/ning/OCR/"
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=666, ssl_context=("./ning.crt", "./ning.key"))
