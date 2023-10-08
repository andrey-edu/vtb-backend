import os

# библиотека для запуска переменных окружения из файла .env
from dotenv import load_dotenv

# активируем переменные окружения из файла .env
load_dotenv()



#* Create connection to MongoDB

# pipenv install motor
from motor.motor_asyncio import AsyncIOMotorClient

# получаем значение переменной
MONGO_USER = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
MONGO_URL = os.environ.get("MONGO_URL")
MONGO_PORT = os.environ.get("MONGO_PORT")

client = AsyncIOMotorClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_URL}:{MONGO_PORT}/")

# get the departments database
vtb = client.vtb