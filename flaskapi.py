#!/usr/bin/python3
from flask import Flask, jsonify, request
import configparser

from translate import baiduTranslator as btt


app = Flask(__name__) # create a server 

@app.route('/get_user',methods=['post']) 
#@app.route('/api/translate',methods=['get']) 
def get_user():
    postdata = request.form.get('word')
    #data  = btt().translateWord('fuck')
    data  = btt().translateWord(postdata)

    return jsonify(data)   # pac as a json

conf = configparser.ConfigParser()
conf.read('conf.ini')
debug = conf.getint('settings', 'debug')

if debug > -1:
    app.run(host='0.0.0.0',port=8802,debug=True)
else:
    app.run(host='0.0.0.0',port=8802,debug=False)
    

'''
#这个host：windows就一个网卡，可以不写，而liux有多个网卡，写成0:0:0可以接受任意网卡信息,
 通过访问127.0.0.1:8802/get_user，可返回data信息
#debug:调试的时候，可以指定debug=true；如果是提供接口给他人使用的时候，debug要去掉
'''
