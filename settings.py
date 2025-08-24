from dotenv import load_dotenv
import os
load_dotenv()
db = os.getenv("DATABASE_URL")
database_users = os.getenv("database_users")
TOKEN=os.getenv('token')
