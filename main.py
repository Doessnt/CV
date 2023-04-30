import os 
import uuid
from flask import Flask, render_template, request, redirect, jsonify
from flask.helpers import make_response, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



if '__main__' == __name__:
    app.run()