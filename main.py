import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

import Services

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

ADMINS = [6335120359, 1217116448]

@dp.message(Command(commands=["start", "help"]))
async def start_cmd(message: Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    await message.answer(f"Assalomu alaykum {user_first_name} sizning id: {user_id}\n"
                         f"Siz bu bot orqali o'z testingizni tekshirib olishingiz mumkin\n"
                         f"Quyidagi shablonda xabar jo'nating\n"
                         f"test_id test_kalitlari\n\n")
    if user_id in ADMINS:
        await message.answer(f"{user_first_name} siz botda qo'shimcha funksiyalardan foydalanishingiz mumkin\n"
                             f"/add_test test_kalitlari\n"
                             f"bu bo'limda faqat test kalitlarini ketma-ket kiritib borasiz\n"
                             f"Quyidagi shablon\n"
                             f"abcd\n"
                             f"Keyin bot sizga alohida test_id beradi uni o'quvchilarga aytasiz\n"
                             f"/show_all_test\n"
                             f"Bu siz qo'shgan barcha testlarni test_id va kalitlarini beradi\n"
                             f"/show_all_act\n"
                             f"Bu bo'lim bo'lsa sizga botga barcha javob jo'natganlar haqida ma'lumot beradi\n"
                             f"/show_all_act test_id\n"
                             f"Bu bo'lim bo'lsa ma'lum test_id ga javob jo'natganlar haqida aytadi\n")

@dp.message(Command("clear"))
async def clear(message: Message):
    if message.from_user.id == 6335120359:
        ans = await Services.clear()
        if ans == 0:
            await message.answer("A'zamjon baza tozalandi")

@dp.message(Command("show_all_act"))
async def show_acts(message: Message):
    if message.from_user.id not in ADMINS:
        await message.answer("/help bo'limiga o'ting")
        return
    path_help = "helper.txt"
    cmd = message.text.split()
    ans = "user_id | test_id | first_name | kalit | ball\n\n"
    acts = await Services.show_all_act()

    if len(cmd) == 1:
        for act in acts:
            ans += act
    else:
        for act in acts:
            if act.split()[1] == cmd[1]:
                ans += act
    with open(path_help, "w") as file:
        file.write(ans)

    await message.answer(ans)
    await message.answer_document(FSInputFile(path_help), caption="Mana file ko'rinishida")

@dp.message(Command("add_test"))
async def add_test_cmd(message: Message):
    if message.from_user.id not in ADMINS:
        await message.answer("@AzamjonAlijonov bilan bog'laning")
        return

    test_key = message.text.split()
    if len(test_key) == 1:
        await message.answer("/help bo'limidagi yo'riqnomadan foydalaning")
    else:
        test_id = await Services.add_test(test_key[1])
        await message.answer(f"{test_id} id bilan test muvaffaqiyatli qo'shildi")


@dp.message(Command("show_all_test"))
async def show_all(message: Message):
    if message.from_user.id not in ADMINS:
        await message.answer("/help bo'limiga o'ting")
        return

    tests = await Services.show_all_test()
    await message.answer(f"{tests}")

@dp.message()
async def check_ans(message: Message):
    ans = message.text.split()
    if len(ans) == 1:
        await message.answer("Javoblarni quyidagi holatda yuboring\n"
                             "test_id test_kalitlari\n"
                             "12 abcd\n")
        return
    chat_id = message.from_user.id
    test_id = ans[0]
    first_name = message.from_user.first_name
    cnt = await Services.add_ans(chat_id, test_id, first_name, ans[1])

    await message.answer(f"Humatli {first_name} siz {test_id} id li tesdan {cnt} ta topdingiz")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())