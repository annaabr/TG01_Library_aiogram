import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды:'
                         '\n /start'
                         '\n /links'
                         '\n /dynamic'
                        )

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=kb.main)

@dp.message(F.text == "Привет")
async def greet(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока")
async def goodbye(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')

@dp.message(Command('links'))
async def show_links(message: Message):
    await message.answer('Выберите ссылку:', reply_markup=kb.links_keyboard)

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Нажмите на кнопку "Показать больше".', reply_markup=kb.dynamic_keyboard)

@dp.callback_query(F.data == "show_more")
async def show_more(callback: CallbackQuery):
    await callback.message.edit_text('Выберите опцию:', reply_markup=kb.more_options_keyboard)

@dp.callback_query(F.data == "option1")
async def option1(callback: CallbackQuery):
    await callback.answer('Вы выбрали Опцию 1.')
    await callback.message.answer('Опция 1')

@dp.callback_query(F.data == "option2")
async def option2(callback: CallbackQuery):
    await callback.answer('Вы выбрали Опцию 2.')
    await callback.message.answer('Опция 2')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())