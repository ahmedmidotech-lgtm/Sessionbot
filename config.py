import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))        # رقم
API_HASH = os.getenv("API_HASH")         # نص
BOT_TOKEN = os.getenv("BOT_TOKEN")       # توكن البوت
OWNER_ID = int(os.getenv("OWNER_ID"))    # رقم ID بتاعك
MONGO_DB_URI = os.getenv("MONGO_DB_URI") # لينك المونجو
