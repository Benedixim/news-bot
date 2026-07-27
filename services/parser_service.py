import time

from parser.sources.itmo import ITMOParser
from repositories.news_repository import NewsRepository


class ParserService:

    def __init__(self):

        self.parsers = [
            ITMOParser(),
        ]

        self.repository = NewsRepository()

    def parse_once(self):

        total = 0

        for parser in self.parsers:

            print(f"Парсинг {parser.__class__.__name__}")

            try:

                news = parser.parse()

                added = self.repository.save_news(
                    source_id=1,
                    news_list=news
                )

                print(f"Добавлено {added}")

                total += added

            except Exception as e:

                print(e)

        print(f"Всего добавлено: {total}")

    def run(self):

        while True:

            try:

                self.parse_once()

            except Exception as e:

                print(e)

            print("Следующий парсинг через 10 минут...")

            time.sleep(600)


if __name__ == "__main__":

    ParserService().run()