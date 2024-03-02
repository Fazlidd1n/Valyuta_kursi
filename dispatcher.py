from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv

load_dotenv()
# BOT_TOKEN = getenv("BOT_TOKEN")
BOT_TOKEN = '6840244701:AAFHix-OsaXfl_Jol7vsc2jE2fedTKXe2II'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
