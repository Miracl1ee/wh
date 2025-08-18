from dotenv import load_dotenv
import os
load_dotenv()
db = os.getenv("DATABASE_URL")
TOKEN=os.getenv('token')
API_URL = os.getenv('API_URL') or "http://192.168.0.152:8000"
TIMEOUT = int(os.getenv('TIMEOUT', 30))
