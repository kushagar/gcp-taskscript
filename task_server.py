from flask import Flask
from flask import send_file
app=Flask(__name__)
@app.route("/healthcheck")
def index():
    return "this is index"
@app.route("/get_message")
def returnimage():
    return "this is a web page"
app.run(host="0.0.0.0",port=80,debug=True)