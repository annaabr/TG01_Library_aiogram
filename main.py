import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

import random

bot = Bot(token = TOKEN)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message: Message):
    list = [
        'https://i.pinimg.com/originals/30/a0/2b/30a02b9d7517d5b27803c8180d8123c6.jpg',
        'https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg',
        'https://i.pinimg.com/originals/e7/17/fd/e717fda07a2e5a8fecaa22dc41db19a5.jpg']
    random_photo = random.choice(list)
    await message.answer_photo(random_photo, caption='Это красивая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Непонятно, что это такое', 'Не отправляй мне такое больше!', 'Ого! Какая красивая фотка!']
    random_answer = random.choice(list)
    await message.answer(random_answer)


@dp.message(F.text == 'Что такое ИИ?')
async def help(message: Message):
    await message.answer('Искусственный интеллект (англ. artificial intelligence; AI) в самом широком смысле — это интеллект, демонстрируемый машинами, в частности компьютерными системами.')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды:\n /start \n /help \n /photo')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Приветики! Я бот!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())