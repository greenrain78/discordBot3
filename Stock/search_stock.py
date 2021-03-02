import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class SearchStock:

    @staticmethod
    def get_soup(company_code) -> BeautifulSoup:
        url = "https://finance.naver.com/item/main.nhn?code=" + company_code
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        return soup

    @classmethod
    def get_price(cls, company_code):
        soup = cls.get_soup(company_code)
        no_today = soup.find("p", {"class": "no_today"})
        blind = no_today.find("span", {"class": "blind"})
        now_price = blind.text
        return now_price

