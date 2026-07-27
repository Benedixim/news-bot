import time

from ai.summarizer import NewsSummarizer

from repositories.news_repository import NewsRepository
from repositories.news_ai_repository import NewsAIRepository


class AIService:

    def __init__(self):

        self.news_repository = NewsRepository()
        self.ai_repository = NewsAIRepository()

        self.ai = NewsSummarizer()

    def process_once(self):

        news_list = self.news_repository.get_new_news()

        print(f"\nНайдено новых новостей: {len(news_list)}")

        for news in news_list:

            print(f"\nОбрабатываю: {news.title}")

            try:

                result = self.ai.summarize(news.text)

                self.ai_repository.save(
                    news.id,
                    result
                )

                #self.news_repository.set_ready(
                #    news.id
                #)

                self.news_repository.set_status(
                    news.id,
                    "READY"
                )

                print("✓ Успешно")

            except Exception as e:

                print(e)

    def run(self):

        while True:

            try:

                self.process_once()

            except Exception as e:

                print(e)

            print("Следующая проверка через 30 секунд...\n")

            time.sleep(30)


if __name__ == "__main__":

    AIService().run()