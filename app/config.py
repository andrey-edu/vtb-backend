import os

# библиотека для запуска переменных окружения из файла .env
from dotenv import load_dotenv

# активируем переменные окружения из файла .env
load_dotenv()



#* Create connection to MongoDB

# pipenv install pymongo
import pymongo

# получаем значение переменной
MONGO_USER = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
MONGO_URL = os.environ.get("MONGO_URL")
MONGO_PORT = os.environ.get("MONGO_PORT")

client = pymongo.MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_URL}:{MONGO_PORT}/")

# print the version of MongoDB server if connection successful
print ("MongoDB server version:", client.server_info()["version"])

# get the database_names from the MongoClient()
# database_names = client.list_database_names()
# print(database_names)

# get the departments database
vtb = client["vtb"]