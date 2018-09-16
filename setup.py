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
        print('you may try: pip install %s'%(re.search(r'\'(.*?)\'', str(e)).group(1))) 


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

try :
    opener = webdriver.Chrome(chrome_options = chrome_options)
    opener.close()
    opener.quit()
except Exception as e:
    print(e)
    if re.search(r'cannot find Chrome binary', str(e)) is not None:
        print('you may install the chrome for your computer')
