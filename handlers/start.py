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
    await message.reply("سلام 🌟\n\n"
    "به پشتیبانی دکتر گشاد خوش اومدی!\n"
    "پیام خودت رو همینجا ارسال کن تا ادمین پاسخ بده.\n"
    "✅ هر پیامی که بدی به صورت خصوصی برای ادمین ارسال میشه و بهت جواب اختصاصی داده میشه.\n"
    "🕒 لطفاً منتظر پاسخ بمون، ما در اسرع وقت پاسخ می‌دیم.\n\n"
    "ممنون که همراهی میکنی 🙏")
