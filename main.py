import asyncio
import logging

from aiogram import Dispatcher, Bot

from apps.start.main import started
from apps.profle.main import profiler

from settings import dp, bot

logger = logging.getLogger(__name__)

#регистрация хендлеров
def register_all_handlers(dp:Dispatcher):
    print('start')
    dp.include_router(profiler)
    dp.include_router(started)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    
    register_all_handlers(dp)
    await dp.start_polling(bot)
    try:
        await dp.start_polling()
    finally:
        print('finally')
        await bot.session.close()
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")