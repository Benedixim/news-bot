from datetime import datetime

from database.database import SessionLocal
from database.models import Notification


class NotificationRepository:

    def exists(self, user_id, news_id):

        session = SessionLocal()

        exists = (
            session.query(Notification)
            .filter(
                Notification.user_id == user_id,
                Notification.news_id == news_id
            )
            .first()
        )

        session.close()

        return exists is not None

    def save(self, user_id, news_id):

        session = SessionLocal()

        session.add(
            Notification(
                user_id=user_id,
                news_id=news_id
                #sent_at=datetime.now()
            )
        )

        session.commit()

        session.close()