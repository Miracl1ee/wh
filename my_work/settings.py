from dotenv import load_dotenv
import os

load_dotenv()

# Проверяем, что переменная загружена
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не найден в .env файле!")

# Для совместимости с вашим кодом
db = DATABASE_URL