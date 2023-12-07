import asyncio
import logging
import sys

from db.config import engine
from dispatcher import dp, bot
from bot import *


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
