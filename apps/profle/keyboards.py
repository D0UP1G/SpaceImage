from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from json import dumps, loads
from aiogram.filters.callback_data import CallbackData

class ProfileCallback(CallbackData, prefix="profile"):
    type: str
    data: str

# profile_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
#         InlineKeyboardButton(text="История", callback_data=ProfileCallback(foo='history').pack()),InlineKeyboardButton(text="UID", callback_data=ProfileCallback(foo='UID').pack())],
#         ])
#(2011652576, 'Goupig', None, 100, '{}')
def profile_keyboards(user:dict):
    # buttons = [[InlineKeyboardButton(text='Турниры', callback_data = ProfileCallback(type='history', data=user[-1]).pack())],
    #             [InlineKeyboardButton(text='Пополнить', callback_data = ProfileCallback(type='donate', data=user[0]).pack()), InlineKeyboardButton(text='Вывести', callback_data=ProfileCallback(type='Withdraw', data=user[0]).pack())]
    #             ]
    buttons = [
    [InlineKeyboardButton(text='Турниры', callback_data=ProfileCallback(type='history', data=str(user[-1])).pack())],
    [InlineKeyboardButton(text='Пополнить', callback_data=ProfileCallback(type='donate', data=str(user[0])).pack()), 
     InlineKeyboardButton(text='Вывести', callback_data=ProfileCallback(type='Withdraw', data=str(user[0])).pack())]]   
    if user[2] == None:
        buttons.append([InlineKeyboardButton(text='Указать UID', callback_data=ProfileCallback(type='UID', data=str(user[0])).pack())  ])
    
    return InlineKeyboardMarkup(inline_keyboard = buttons)

def tournaments_history(tournaments:str):
    tournaments = loads(tournaments)
    buttons = []
    for key in tournaments:
        buttons.append([InlineKeyboardButton(text=key, callback_data=ProfileCallback(type='tournament', data=str(tournaments[key])).pack())])
    buttons.append([InlineKeyboardButton(text='назад', callback_data=ProfileCallback(type='back', data='profile').pack())])
    return InlineKeyboardMarkup(inline_keyboard = buttons)