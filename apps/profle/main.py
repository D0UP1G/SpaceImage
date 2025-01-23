from aiogram import Router, types, F
from sql.DB import BD
from aiogram.filters import Command
from .keyboards import profile_keyboards, ProfileCallback, tournaments_history
from aiogram.fsm.state import StatesGroup, State
from json import dumps

bd = BD('data.db')
profiler = Router()
class Profile(StatesGroup):
    UID = State()


@profiler.message(Command('profile'))
async def profile(msg:types.Message):
    user = bd.get_user(id = msg.from_user.id)
    await msg.answer(f"""
                     Никнейм: 
UID: {'Нету' if user[2] == None else user[2]}
Заработал {user[3]} рублей
    """, reply_markup = profile_keyboards(user))
    
from aiogram.types.callback_query import CallbackQuery    

@profiler.callback_query(ProfileCallback.filter(F.type == 'history'))
async def process_yes_callback(query: CallbackQuery,callback_data: ProfileCallback):

    user = bd.get_user(id = query.message.from_user.id)
    await query.message.answer('Ваши турниры', reply_markup=tournaments_history(dumps({'Хеллоуин турнир на 1000000 гемов':1232123})))
    await query.message.delete()

@profiler.callback_query(ProfileCallback.filter(F.type == 'back'))
async def back(query: CallbackQuery,callback_data: ProfileCallback):
    user = bd.get_user(id = query.from_user.id)
    await query.message.delete()
    if callback_data.data == 'profile':
        await query.message.answer(f"""
                     Никнейм: 
UID: {'Нету' if user[2] == None else user[2]}
Заработал {user[3]} рублей
    """, reply_markup = profile_keyboards(user))
        

@profiler.callback_query(ProfileCallback.filter(F.type == 'tournament'))
async def tournament(query: CallbackQuery,callback_data: ProfileCallback):
    await query.message.delete()
    print(callback_data.data)
    await query.message.answer('Hello')