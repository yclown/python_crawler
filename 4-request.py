# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup as bf
if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = bf(req.text)
    texts = html.find_all('div', id= 'content') 
    print(texts)
