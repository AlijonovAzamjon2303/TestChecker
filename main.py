import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message

import Services

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

tests = {}
ADMIN = 6335120359

@dp.message(Command("start"))
async def start_cmd(message: Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    await message.answer(f"Assalomu alaykum {user_first_name} sizning id: {user_id}")
    await message.answer("Quyidagi buyruqlardan birini tanlang\n/add_test\n/check_test")

@dp.message(Command("add_test"))
async def add_test_cmd(message: Message):
    if message.from_user.id == ADMIN:
        await message.answer("1a2b3c4d ... kabi test javoblarini kiriting")
    else:
        await message.answer("@AzamjonAlijonov bilan bog'laning")

@dp.message(Command("show_all_test"))
async def show_all(message: Message):
    await message.answer(f"{Services.show_all_test()}")

@dp.message(lambda message: message.from_user.id == ADMIN)
async def save_test(message: Message):
    test_keys = message.text.strip()  # Test javoblarini olish
    print(f"Admin test javoblari: {test_keys}")  # Admin tomonidan yuborilgan test javoblarini konsolga chiqarish

    try:
        test_id = await Services.add_test(test_keys)  # Testni saqlash
        print(f"Test ID: {test_id}")  # Yangi test ID sini konsolga chiqarish
        await message.answer(f"Test {test_id} bilan saqlandi")  # Adminni xabardor qilish
    except Exception as e:
        print(f"Xatolik: {e}")  # Xatolik yuz bersa, uni konsolga chiqarish
        await message.answer("Testni saqlashda xatolik yuz berdi!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())