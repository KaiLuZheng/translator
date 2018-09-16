#!/usr/bin/python3

import re

try:
    import flask
    print('import flask ok!')

    import selenium
    print('import selenium ok!')

    from bs4 import BeautifulSoup
    print('import BeautifulSoup ok!')

except Exception as e:
    print(e)

    if re.search(r'No module', str(e)) is not None:
        print('you may try: pip install %s'%(re.search(r'\'(.*?)\'').group(1))) 


