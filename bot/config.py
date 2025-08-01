import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_BASIC = os.getenv("ADMIN_BASIC")
ADMIN_TECH = os.getenv("ADMIN_TECH")
ADMIN_SALES = os.getenv("ADMIN_SALES")