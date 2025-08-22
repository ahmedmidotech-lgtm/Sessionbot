import os
from dotenv import load_dotenv

# تحميل بيانات .env
load_dotenv()

API_ID = int(os.getenv("API_ID"))           # لازم يبقى رقم صحيح
API_HASH = os.getenv("API_HASH")            # نص طويل
BOT_TOKEN = os.getenv("BOT_TOKEN")          # التوكن بتاع البوت
OWNER_ID = int(os.getenv("OWNER_ID"))       # رقم ID بتاعك
MONGO_DB_URI = os.getenv("MONGO_DB_URI")    # لينك قاعدة بيانات مونجو
