import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import sqlite3
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import logging

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    age = State()
    grade = State()

def init_db():
    conn = sqlite3.connect('school_data.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS school_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL)
        ''')
    conn.commit()
    conn.close()

init_db()

@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer('Привет, как тебя зовут?')
    await state.set_state(Form.name)

@dp.message(Form.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Сколько тебе лет?')
    await state.set_state(Form.age)

@dp.message(Form.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('В каком классе ты учишься?')
    await state.set_state(Form.grade)

@dp.message(Form.grade)
async def grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    student_data = await state.get_data()

    conn = sqlite3.connect('school_data.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO school_data (name, age, grade) values (?,?,?)''',(student_data['name'], student_data['age'], student_data['grade']))
    conn.commit()
    conn.close()

    student_report = ('В базу данных добавлена информация о новом студенте:\n'
                      f'Имя - {student_data["name"]}\n'
                      f'Возраст - {student_data['age']}\n'
                      f'Класс - {student_data['grade']}')
    await message.answer(student_report)
    await state.clear()

@dp.message(Command('showschool'))
async def show_school(message: Message):
    conn = sqlite3.connect('school_data.db')
    cur = conn.cursor()
    cur.execute('SELECT name, age, grade FROM school_data')
    rows = cur.fetchall()
    conn.close()

    if rows:
        response = "Содержимое базы данных:\n"
        for row in rows:
            response += f'Имя: {row[0]}, Возраст: {row[1]}, Класс: {row[2]}\n'
    else:
        response = "База данных пуста."

    await message.answer(response)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())