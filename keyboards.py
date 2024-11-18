from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text="Тестовая кнопка 1")],
[KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/watch?v=EmAO8f_l-F4")],
    [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
    [InlineKeyboardButton(text="Новости", callback_data="news")],
    [InlineKeyboardButton(text="Профиль", callback_data="person")]
])



test = ["Кнопка 1", "Кнопка 2", "Кнопка 3", "Кнопка 4"]

'''
async def test_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for key in test:
        keyboard.add(KeyboardButton(text=key))
    return keyboard.adjust(2).as_markup()
'''

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key,url="https://google.com"))
    return keyboard.adjust(2).as_markup()
