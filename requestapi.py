#!/usr/bin/python3 

import urllib
import urllib.request
import json

url = 'http://www.lumeno.club:8080/api/translate'
url = 'http://localhost:8080/api/translate'

word = input('word:')

param = {
    'word' : word
}

#data = urllib.parse.urlencode(word).encode()

# for json
data = json.dumps(param)
data = bytes(data, 'utf8')

req = urllib.request.Request(url, data = data)
res = urllib.request.urlopen(req)

response = res.read().decode('utf8')

sjson = json.loads(response)
print(sjson)
