from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Основная клавиатура
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет")],
    [KeyboardButton(text="Пока")]
], resize_keyboard=True)

# Клавиатура с ссылками
links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://ria.ru/")],
    [InlineKeyboardButton(text="Музыка", url="https://zvuk.com/")],
    [InlineKeyboardButton(text="Видео", url="https://rutube.ru/feeds/mashabear/")]
])

# Динамическая клавиатура
dynamic_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
])

# Клавиатура с дополнительными опциями
more_options_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data="option1")],
    [InlineKeyboardButton(text="Опция 2", callback_data="option2")]
])