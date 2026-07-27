import json

from database.database import SessionLocal
from database.models import NewsAI


import json


class NewsAIRepository:

    def save(self, news_id, ai):

        session = SessionLocal()

        exists = (
            session.query(NewsAI)
            .filter(NewsAI.news_id == news_id)
            .first()
        )

        if exists:
            session.close()
            return

        model = NewsAI(
            news_id=news_id,
            ai_title=ai["title"],
            summary=ai["summary"],
            deadline=ai["deadline"],
            categories=json.dumps(
                ai["categories"],
                ensure_ascii=False
            )
        )

        session.add(model)
        session.commit()
        session.close()



    def get_by_news(self, news_id):

        session = SessionLocal()

        row = (
            session.query(NewsAI)
            .filter(
                NewsAI.news_id == news_id
            )
            .first()
        )

        session.close()

        if row is None:
            return None

        row.categories = json.loads(row.categories)

        return row
