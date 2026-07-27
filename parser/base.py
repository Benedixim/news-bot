from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class BaseParser(ABC):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    def get_soup(self, url):

        response = requests.get(
            url,
            headers=self.headers,
            timeout=20
        )

        response.raise_for_status()
        with open("itmo.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        #print("HTML сохранен в itmo.html")

        return BeautifulSoup(response.text, "lxml")
        

    @abstractmethod
    def parse(self):
        pass