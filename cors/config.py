import os
from dotenv import load_dotenv


class Settings:
    origins = os.getenv("ORIGINS", "*").split(",")


settings = Settings()
