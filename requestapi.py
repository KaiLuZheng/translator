#!/usr/bin/python3 

import urllib
import urllib.request
import json

url = 'http://localhost:8802/get_user'

word = input('word:')

param = {
    'word' : word
}

data = urllib.parse.urlencode(param).encode()

req = urllib.request.Request(url, data)
res = urllib.request.urlopen(req)

sjson = json.loads(res.read().decode('utf8'))

print(sjson)
