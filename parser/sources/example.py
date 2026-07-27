from parser.base import BaseParser


class ExampleParser(BaseParser):

    def parse(self):

        return [
            {
                "title": "Первая новость",
                "text": "Текст первой новости",
                "url": "https://example.com/news/1",
                "published_at": "2026-07-22"
            },
            {
                "title": "Вторая новость",
                "text": "Текст второй новости",
                "url": "https://example.com/news/2",
                "published_at": "2026-07-22"
            }
        ]