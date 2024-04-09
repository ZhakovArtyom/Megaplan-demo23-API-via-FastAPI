from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс Settings подгружает данные из файла .env."""

    MEGAPLAN_API_KEY: str
    USER_ID: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
