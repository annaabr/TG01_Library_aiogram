import asyncio
import random
import aiohttp  # Библиотека для асинхронных HTTP-запросов
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from gtts import gTTS
import os

from config import TOKEN, WEATHER_API_KEY  # Добавьте WEATHER_API_KEY в ваш файл config.py

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('train.ogg')
    await message.answer_voice(voice)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('TG02.pdf')
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('audio'))
async def audio(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_audio')
    audio = FSInputFile('audio.mp3')
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('training'))
async def training(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_voice')
    training_list = [
        'Тренировка 1.\nКруговые движения руками (30 секунд вперед и назад),\nНаклоны головы (вперед, назад, в стороны),\nПрыжки на месте (1 минута)',
        'Тренировка 2.\nПриседания (1 минута),\nОтжимания (1 минута),\nВыпады (по 30 секунд на каждую ногу).',
        'Тренировка 3.\nЛегкий бег на месте или прыжки на скакалке,\n30 секунд планки с отжиманием,\n30 секунд скручиваний.'
    ]
    rand_tr=random.choice(training_list)
    await message.answer(f"Это Ваша тренировка на сегодня:\n{rand_tr}")

    # Отправка тренировки в формате звукового файла
    # tts = gTTS(text=rand_tr, lang='ru')
    # tts.save('training.mp3')
    # audio = FSInputFile('training.mp3')
    # await bot.send_audio(message.chat.id, audio)
    # os.remove(('training.mp3'))

    # Отправка тренировки в виде звукового сообщения
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.ogg')
    audio = FSInputFile('training.ogg')
    await bot.send_voice(message.chat.id, audio)
    # os.remove(('training.ogg'))


# @dp.message(Command('photo', prefix='&'))
@dp.message(Command('photo'))
async def photo(message: Message):
    list = [
        'https://i.pinimg.com/originals/30/a0/2b/30a02b9d7517d5b27803c8180d8123c6.jpg',
        'https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg'    'https://i.pinimg.com/originals/e7/17/fd/e717fda07a2e5a8fecaa22dc41db19a5.jpg']
    random_photo = random.choice(list)
    await message.answer_photo(random_photo, caption='Это красивая картинка с котиком!')


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Непонятно, что это такое', 'Не отправляй мне такое больше!', 'Ого! Какая красивая фотка!']
    random_answer = random.choice(list)
    await message.answer(random_answer)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')


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
                         '\n /video'
                         '\n /audio'
                         '\n /doc '
                         '\n /voice'
                         '\n /training '
                         '\n Бот также умеет отвечать на вопрос "Что такое ИИ?"',)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.full_name}! Я бот!')


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

@dp.message()
async def start(message: Message):
    # await message.answer('Это мой ответ тебе!')
    if message.text.lower() == 'тест':
        await message.answer('Проводится тестирование возможностей бота!')
    else:
        await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())