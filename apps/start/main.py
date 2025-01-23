from aiogram import Router, types
from sql.DB import BD
from aiogram.filters import CommandStart

bd = BD('data.db')
started = Router()

@started.message(CommandStart())
async def start(msg:types.Message):
    bd.first_user(msg.from_user.id, msg.from_user.username)
    await msg.answer('Приветствую тебя в проекте Fun Game\nPS. приятной игры <3')
