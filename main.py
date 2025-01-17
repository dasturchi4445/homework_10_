import logging

from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard, menu_detail, mahsulot_button

from db import Database

API_TOKEN = "7361801423:AAFbDRViSXi0eq-JC4Fg8t4dfjmX2uE-NnE"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2 (username, full_name, user_id) VALUES ('{username}', '{ful_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursandman  {ful_name}", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {ful_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("1 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Menyu 2")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Menyu 3")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Menyu 4")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Menyu 5")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Menyu 6")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Menyu 7")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Menyu 8")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Mahsulot 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=mahsulot_button)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    if message.from_user.id in [1001968950]:
        await message.reply("Salom admin")
        photo_path = "https://www.google.co.uz/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2Fnajotedu%2F%3Flocale%3Dru_RU&psig=AOvVaw2zDxN9-lq0M-FsUnKQwp3M&ust=1718989969065000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCBte7W6oYDFQAAAAAdAAAAABAE"
        await bot.send_photo(message.chat.id, photo=photo_path)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

# class smt():
# def ofmaofmsaofeimaof;simfa
