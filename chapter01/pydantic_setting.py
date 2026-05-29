import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
	host: str
	port: int
	db_url: str
	timeout: int
	model_config = SettingsConfigDict(env_prefix="APP_")
	
def load_settings() -> AppSettings:
	os.environ["APP_HOST"] = "localhost"
	os.environ["APP_PORT"] = "8080"
	os.environ["APP_DB_URL"] = "postgresql://user:password@localhost:5432/mydb"
	os.environ["APP_TIMEOUT"] = "30"
	
	return AppSettings()


if __name__ == "__main__":
	u = load_settings()
	print(u.model_dump_json())
