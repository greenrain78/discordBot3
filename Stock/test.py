import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_code(company_code) -> BeautifulSoup:
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def get_price(company_code):
    soup = get_code(company_code)
    no_today = soup.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    now_price = blind.text
    return now_price


company_codes = ["005930"]

while True:
    now = datetime.now()
    print(now)

    for item in company_codes:
        now_price = get_price(item)
        print(now_price)
    print("---------------------------------")
    time.sleep(60)