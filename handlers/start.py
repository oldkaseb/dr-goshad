from aiogram import types
from config import ADMIN_ID
from utils.db import add_user

async def start_handler(message: types.Message):
    user = message.from_user
    add_user({
        "id": user.id,
        "name": user.full_name,
        "username": user.username,
        "start_time": message.date.isoformat()
    })
    await message.reply("سلام! پیام خود را ارسال کنید تا ادمین پاسخ دهد.")
