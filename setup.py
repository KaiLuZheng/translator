#!/usr/bin/python3

try:
    import flask
    print('import flask ok!')

    import selenium
    print('import selenium ok!')

    from bs4 import BeautifulSoup
    print('import BeautifulSoup ok!')

except Exception as e:

    print(e)


