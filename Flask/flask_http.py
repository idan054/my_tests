from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Resource, Api
import requests
import json
import telegram_send

from pywebcopy import save_webpage

kwargs = {'project_name': 'some-fancy-name'}

save_webpage(
    url='http://www.stips.co.il/',
    project_folder='../google',
    **kwargs
)

app = Flask(__name__)
api  = Api(app)


# class Student (Resource) :
#     # @staticmethod
#     @app.route('/student/<string:name>')
#     def get(name):
#         return {'student':name}

@app.route("/isUserOnline")
def isUserOnline(): # Def name doesnt matter

    return soup
# api.add_resource (Student, '/student/<string:name>') # http://127. e.0. 1: 5000/student/Rolf
app.run(port=5000)