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
                         '\n /start '
                         '\n /help '
                        )


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}! Я бот!',
                         reply_markup=kb.inline_keyboard_test)


@dp.message(F.text == "Тестовая кнопка 1")
async def test_button(message: Message):
   await message.answer('Обработка нажатия на reply кнопку')

@dp.callback_query(F.data == "news")
async def news(callback: CallbackQuery):
    # await callback.answer("Новости подгружаются")
    await callback.answer("Новости подгружаются", show_alert=True)
    # await callback.message.answer('Вот свежие новости!')
    await callback.message.edit_text('Вот свежие новости!',reply_markup=await kb.inline_keyboard_test)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())