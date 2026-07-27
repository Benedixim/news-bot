from database.database import SessionLocal
from database.models import Source


class SourceRepository:

    def get_enabled_sources(self):

        session = SessionLocal()

        sources = (
            session.query(Source)
            .filter(Source.enabled == True)
            .all()
        )

        session.close()

        return sources

    def create_if_not_exists(self, name, url, parser):

        session = SessionLocal()

        exists = (
            session.query(Source)
            .filter(Source.parser == parser)
            .first()
        )

        if exists:
            session.close()
            return

        source = Source(
            name=name,
            url=url,
            parser=parser,
            enabled=True
        )

        session.add(source)
        session.commit()
        session.close()