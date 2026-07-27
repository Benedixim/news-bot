import json

from fastapi import FastAPI

from database.database import SessionLocal
from database.models import News, NewsAI

app = FastAPI()


import json

from fastapi import FastAPI
from fastapi import Query

from database.database import SessionLocal
from database.models import News, NewsAI

app = FastAPI()


@app.get("/news")
def get_news(

        course: str | None = None,

        specialization: str | None = None,

        language: str | None = None,

        location: str | None = None,

        price: str | None = None

):

    session = SessionLocal()

    rows = (
        session.query(News, NewsAI)
        .join(NewsAI, News.id == NewsAI.news_id)
        .all()
    )

    result = []

    for news, ai in rows:

        categories = json.loads(ai.categories)

        if course:

            if course not in categories["course"]:
                continue

        if specialization:

            if specialization not in categories["specialization"]:
                continue

        if language:

            if language not in categories["language"]:
                continue

        if location:

            if location not in categories["location"]:
                continue

        if price:

            if price != categories["price"]:
                continue

        result.append(
            {
                "title": ai.ai_title,
                "summary": ai.summary,
                "deadline": ai.deadline,
                "categories": categories,
                "url": news.url
            }
        )

    session.close()

    return result




from pydantic import BaseModel

class UserRequest(BaseModel):

    telegram_id: int

    username: str | None = None

    filters: dict


from repositories.user_repository import UserRepository

repo = UserRepository()


@app.post("/users")
def create_user(user: UserRequest):

    repo.save_user(
        user.telegram_id,
        user.username,
        user.filters
    )

    return {
        "status": "ok"
    }


class FilterRequest(BaseModel):

    course: list

    specialization: list

    price: str

    location: list

    language: list


@app.post("/users/news")
def news(filters: FilterRequest):

    session = SessionLocal()

    rows = (
        session.query(News, NewsAI)
        .join(
            NewsAI,
            News.id == NewsAI.news_id
        )
        .all()
    )

    result = []

    for news, ai in rows:

        categories = json.loads(ai.categories)

        ok = True

        if filters.course:

            if not any(
                x in categories["course"]
                for x in filters.course
            ):
                ok = False

        if filters.specialization:

            if not any(
                x in categories["specialization"]
                for x in filters.specialization
            ):
                ok = False

        if filters.location:

            if not any(
                x in categories["location"]
                for x in filters.location
            ):
                ok = False

        if filters.language:

            if not any(
                x in categories["language"]
                for x in filters.language
            ):
                ok = False

        if filters.price:

            if filters.price != categories["price"]:
                ok = False

        if ok:

            result.append(
                {
                    "title": ai.ai_title,
                    "summary": ai.summary,
                    "deadline": ai.deadline,
                    "url": news.url
                }
            )

    session.close()

    return result