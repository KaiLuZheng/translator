#!/usr/bin/python3
from flask import Flask, jsonify, request
import configparser

from translate import baiduTranslator as btt


app = Flask(__name__) # create a server 

@app.route('/api/translate',methods=['post']) 
#@app.route('/api/translate',methods=['get']) 
def get_user():
    postdata = request.form.get('word')
    #data  = btt().translateWord('fuck')
    data  = btt().translateWord(postdata)

    return jsonify(data)   # pack as a json

@app.route('/',methods=['get']) 
def index():
    with open('./htmls/index.html', 'r') as f:
        return f.read()  


conf = configparser.ConfigParser()
conf.read('conf.ini')
debug = conf.getint('settings', 'debug')

if debug > -1:
    app.run(host='0.0.0.0',port=8802,debug=True)
else:
    app.run(host='0.0.0.0',port=8802,debug=False)
