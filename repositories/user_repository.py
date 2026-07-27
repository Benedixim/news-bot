import json

from database.database import SessionLocal
from database.models import User


class UserRepository:

    def save_user(
        self,
        telegram_id,
        username,
        filters
    ):

        session = SessionLocal()

        user = (
            session.query(User)
            .filter(User.telegram_id == telegram_id)
            .first()
        )

        if user is None:

            user = User(
                telegram_id=telegram_id,
                username=username,
                filters=json.dumps(
                    filters,
                    ensure_ascii=False
                )
            )

            session.add(user)

        else:

            user.filters = json.dumps(
                filters,
                ensure_ascii=False
            )

        session.commit()

        session.close()

    def get_all(self):

        session = SessionLocal()

        users = session.query(User).all()

        session.close()

        return users