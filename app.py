from flask import Flask, render_template, send_file
import subprocess
import os
import datetime
import time
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def hello():

   return render_template('index.html')


@app.route("/takeimg/")
def takeimg():
   subprocess.call(['./run'], shell=True )

   img_dir = os.getcwd() + '/img2gcode/output/'
   img_jpg = send_file(img_dir +"tmp.jpg")
   img_svg = send_file( img_dir + "tmp.svg")
   gcode = None
   with open("./img2gcode/output/tmp.gcode", "r") as f:
      gcode = f.read()

   return render_template('infotaken.html')

#@app.route("/omxstop/")
#def omxstop():
#   subprocess.call(['./omxstop.sh'], shell=True)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)