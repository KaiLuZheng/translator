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

try :
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    opener = webdriver.Chrome(chrome_options = chrome_options)
except Exception as e:
    print(e)
finally:
    opener.close()
    opener.quit()
    
