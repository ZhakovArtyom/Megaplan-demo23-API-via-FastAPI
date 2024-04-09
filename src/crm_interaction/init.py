from src.crm_interaction.http_client import MegaplanHTTPClient
from config import settings


# инициализация объекта MegaplanHTTPClient для работы в эндпоинтах
megaplan_client = MegaplanHTTPClient(
    base_url="https://demo23.megaplan.ru",
    api_key=settings.MEGAPLAN_API_KEY
)
