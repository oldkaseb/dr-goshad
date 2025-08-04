from aiogram import types
from utils.db import add_user

async def start_handler(message: types.Message):
    user = message.from_user

    add_user({
        "id": user.id,
        "name": user.full_name,
        "username": user.username or "",
        "start_time": message.date.isoformat()
    })

    await message.reply(
        "سلام 👋\n\n"
        "به ربات دکتر گشاد خوش اومدی.\n"
        "پیام خودت رو بفرست تا به ادمین منتقل بشه. ✉️\n"
        "لطفاً صبور باش تا پاسخ داده بشه 💬"
    )
