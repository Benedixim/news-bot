import asyncio
import os

from aiohttp import ClientSession
from dotenv import load_dotenv

load_dotenv()


class KeepAliveService:

    def __init__(self):
        self.url = os.getenv(
            "KEEPALIVE_URL",
            "https://news-bot-gckb.onrender.com"
        )

    async def run(self):

        while True:

            try:

                async with ClientSession() as session:

                    async with session.get(self.url) as response:

                        print(
                            f"[KeepAlive] {response.status}"
                        )

            except Exception as e:

                print(
                    f"[KeepAlive] {e}"
                )

            await asyncio.sleep(300)


if __name__ == "__main__":

    asyncio.run(
        KeepAliveService().run()
    )