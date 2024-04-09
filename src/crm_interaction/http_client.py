from aiohttp import ClientSession
from config import settings
from async_lru import alru_cache


class HTTPClient:
    """
    Базовый класс для взаимодействия с API.

    Инициализирует сессию для выполнения HTTP-запросов, автоматически добавляя
    базовый URL и API ключ в заголовки запроса.
    """

    def __init__(self, base_url: str, api_key: str) -> None:
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'Authorization': f"Bearer {api_key}",
            }
        )


class MegaplanHTTPClient(HTTPClient):
    """
    Класс для кастомного взаимодействия с API Megaplan.

    Реализует специфичные методы для получения данных, используя кэширование
    для повышения производительности.
    """

    @alru_cache
    async def get_credentials(self):
        async with self._session.get(
            f"/api/v3/contractorHuman/{settings.USER_ID}"
        ) as resp:
            result = await resp.json()
            return (
                result["data"]["Category183CustomFieldLogin"],
                result["data"]["Category183CustomFieldPassword"]
            )

    @alru_cache
    async def get_username(self):
        async with self._session.get(
            f"/api/v3/contractorHuman/{settings.USER_ID}"
        ) as resp:
            result = await resp.json()
            return result["data"]["firstName"]
