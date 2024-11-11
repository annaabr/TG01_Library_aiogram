import asyncio
import random
import aiohttp  # Библиотека для асинхронных HTTP-запросов
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN, WEATHER_API_KEY  # Добавьте WEATHER_API_KEY в ваш файл config.py

bot = Bot(token=TOKEN)
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
    await message.answer(
        'Искусственный интеллект (англ. artificial intelligence; AI) в самом широком смысле — это интеллект, демонстрируемый машинами, в частности компьютерными системами.')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды:'
                         '\n /start '
                         '\n /help '
                         '\n /photo '
                         '\n /weather' 
                         '\n Бот также умеет отвечать на вопрос "Что такое ИИ?"')


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Приветики! Я бот!')


@dp.message(Command('weather'))
async def weather(message: Message):
    city = 'Rostov-on-Don'  # Укажите город
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                weather_description = data['weather'][0]['description']
                await message.answer(
                    f'Погода в Ростове-на-Дону:\nТемпература: {temp}°C\nОписание: {weather_description.capitalize()}')
            else:
                await message.answer('Не удалось получить данные о погоде.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())