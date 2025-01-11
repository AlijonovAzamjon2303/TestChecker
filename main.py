import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

tests = {}
test_id = 1000
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
        await message.answer("Test qo'shishingiz mumkin")
    else:
        await message.answer("@AzamjonAlijonov bilan bog'laning")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())