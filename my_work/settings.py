from dotenv import load_dotenv
import os
load_dotenv()
db = os.getenv("DATABASE_URL")
TOKEN=os.getenv('token')

