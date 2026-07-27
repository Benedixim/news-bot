from sqlalchemy.exc import IntegrityError

from database.database import SessionLocal
from database.models import News


class NewsRepository:

    def save_news(self, source_id, news_list):

        session = SessionLocal()

        added = 0

        for item in news_list:

            news = News(
                source_id=source_id,
                title=item["title"],
                text=item["text"],
                url=item["url"],
                published_at=item["published_at"],
                status="NEW"
            )

            try:

                session.add(news)
                session.commit()

                added += 1

            except IntegrityError:

                session.rollback()

        session.close()

        return added

    def get_new_news(self):

        session = SessionLocal()

        news = (
            session.query(News)
            .filter(News.status == "NEW")
            .all()
        )

        session.close()

        return news

    def get_ready_news(self):

        session = SessionLocal()

        news = (
            session.query(News)
            .filter(News.status == "READY")
            .all()
        )

        session.close()

        return news

    def set_status(self, news_id, status):

        session = SessionLocal()

        news = session.get(News, news_id)

        if news:

            news.status = status
            session.commit()

        session.close()