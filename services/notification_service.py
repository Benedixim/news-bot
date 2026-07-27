import asyncio
import json
import os

from aiogram import Bot
from dotenv import load_dotenv

from bot.templates import news_message

from repositories.news_repository import NewsRepository
from repositories.news_ai_repository import NewsAIRepository
from repositories.user_repository import UserRepository
from repositories.notification_repository import NotificationRepository

load_dotenv()


class NotificationService:

    def __init__(self):

        self.bot = Bot(os.getenv("BOT_TOKEN"))

        self.news_repository = NewsRepository()
        self.ai_repository = NewsAIRepository()
        self.user_repository = UserRepository()
        self.notification_repository = NotificationRepository()

    def match(self, user_filters, news_categories):

        # курс
        if user_filters.get("course"):
            if not any(
                value in news_categories.get("course", [])
                for value in user_filters["course"]
            ):
                return False

        # специальность
        if user_filters.get("specialization"):
            if not any(
                value in news_categories.get("specialization", [])
                for value in user_filters["specialization"]
            ):
                return False

        # язык
        if user_filters.get("language"):
            if not any(
                value in news_categories.get("language", [])
                for value in user_filters["language"]
            ):
                return False

        # локация
        if user_filters.get("location"):
            if not any(
                value in news_categories.get("location", [])
                for value in user_filters["location"]
            ):
                return False

        # платность
        if user_filters.get("price") != "both":

            if user_filters.get("price") != news_categories.get("price"):
                return False

        return True

    async def send_once(self):

        news = self.news_repository.get_ready_news()

        users = self.user_repository.get_all()

        print(f"READY новостей: {len(news)}")
        print(f"Пользователей: {len(users)}")

        for article in news:

            ai = self.ai_repository.get_by_news(article.id)

            if ai is None:
                continue

            categories = ai.categories

            for user in users:

                # уже отправляли?
                if self.notification_repository.exists(
                    user.id,
                    article.id
                ):
                    continue

                filters = json.loads(user.filters)

                if not self.match(filters, categories):
                    continue

                try:

                    await self.bot.send_message(
                        chat_id=user.telegram_id,
                        text=news_message(
                            {
                                "title": ai.ai_title,
                                "summary": ai.summary,
                                "deadline": ai.deadline,
                                "url": article.url
                            }
                        ),
                        parse_mode="HTML"
                    )

                    self.notification_repository.save(
                        user.id,
                        article.id
                    )

                    print(
                        f"Отправлено пользователю {user.telegram_id}: {ai.ai_title}"
                    )

                #except Exception as e:

                #    print(
                #        f"Ошибка отправки пользователю {user.telegram_id}: {e}"
                #    )

                except Exception as e:

                    print(type(e))
                    print(e)

                    import traceback
                    traceback.print_exc()

    async def run(self):

        while True:

            try:

                await self.send_once()

            except Exception as e:

                print(f"Ошибка NotificationService: {e}")

            print("Следующая проверка через 30 секунд...\n")

            await asyncio.sleep(30)


if __name__ == "__main__":

    asyncio.run(
        NotificationService().run()
    )