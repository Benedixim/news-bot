import httpx

#API = "http://127.0.0.1:8000"

API = "http://127.0.0.1:10000"


async def save_user(
    telegram_id,
    username,
    filters
):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{API}/users",
            json={
                "telegram_id": telegram_id,
                "username": username,
                "filters": filters
            }
        )

        response.raise_for_status()


async def get_news(filters):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{API}/users/news",
            json=filters
        )

        response.raise_for_status()

        return response.json()