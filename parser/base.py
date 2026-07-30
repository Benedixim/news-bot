from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class BaseParser(ABC):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    DEBUG = False

    def get_soup(self, url):

        response = requests.get(
            url,
            headers=self.headers,
            timeout=20
        )

        response.raise_for_status()

        if self.DEBUG:

            filename = self.__class__.__name__ + ".html"

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(response.text)

            print(f"HTML сохранен в {filename}")

        return BeautifulSoup(
            response.text,
            "lxml"
        )

    @abstractmethod
    def parse(self):
        pass