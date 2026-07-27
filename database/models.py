from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from database.database import Base


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    url = Column(String, nullable=False)

    parser = Column(String, nullable=False)

    enabled = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)

    source_id = Column(Integer, ForeignKey("sources.id"))

    title = Column(String)

    text = Column(Text)

    url = Column(String, unique=True)

    published_at = Column(String)

    status = Column(String, default="NEW")

    created_at = Column(DateTime, server_default=func.now())


class NewsAI(Base):

    __tablename__ = "news_ai"

    id = Column(Integer, primary_key=True)

    news_id = Column(Integer, ForeignKey("news.id"), unique=True)

    ai_title = Column(String)

    summary = Column(Text)

    deadline = Column(String)

    categories = Column(Text)

    created_at = Column(DateTime, server_default=func.now())


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    telegram_id = Column(String, unique=True)

    username = Column(String)

    filters = Column(Text)

    created_at = Column(DateTime, server_default=func.now())


class Notification(Base):

    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    news_id = Column(Integer, ForeignKey("news.id"))

    sent_at = Column(DateTime, server_default=func.now())