#!/usr/bin/python3
#-*- encoding: utf8 -*-


import web
from translate import baiduTranslator as bdt
import json


urls = ( 
    '/api/translate', 'translate'
)


class translate:
    def GET(self):
        word = web.input().word
        data = bdt().translateWord(word)
        return json.dumps(data)
        

    def POST(self):
        param = json.loads(web.data().decode('utf8'))
        word = param['word']
        data = bdt().translateWord(word)
        return json.dumps(data)


app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()






