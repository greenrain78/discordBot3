import time
import urllib
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_code(company_code) -> BeautifulSoup:
    word_encode = urllib.parse.quote(company_code)
    url = "https://finance.daum.net/domestic/search?q=" + word_encode
    # url = "https://finance.naver.com/item/main.nhn?code=" + word_encode
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def get_price(company_code):
    soup = get_code(company_code)
    no_today = soup.find("th", {"class": "no1"})
    # blind = no_today.find("span", {"class": "blind"})
    return no_today


# company_codes = ["005930"]

# print(get_price("삼성전자"))
print(get_code("삼성전자"))
