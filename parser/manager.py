import importlib

from repositories.news_repository import NewsRepository
from repositories.source_repository import SourceRepository


class ParserManager:

    def __init__(self):

        self.source_repository = SourceRepository()
        self.news_repository = NewsRepository()

    def run(self):

        sources = self.source_repository.get_enabled_sources()

        if not sources:
            print("Нет активных источников")
            return
        

        for source in sources:

            print(f"\n====== {source.name} ======")

            module = importlib.import_module(
                f"parser.sources.{source.parser}"
            )

            class_name = "".join(
                part.capitalize()
                for part in source.parser.split("_")
            ) + "Parser"

            parser_class = getattr(module, class_name)

            parser = parser_class()

            news = parser.parse()

            count = self.news_repository.save_news(
                source.id,
                news
            )

            print(f"Добавлено {count} новых новостей")