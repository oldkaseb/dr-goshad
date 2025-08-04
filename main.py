### ✅ فایل کامل و نهایی: main.py

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.messages import user_message_handler, admin_reply_callback, block_user_callback
from handlers.commands import stats_handler, forall_handler, add_admin_handler, remove_admin_handler, reply_handler
from utils.state import get_reply

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 📌 هندلرهای کامندها
dp.register_message_handler(start_handler, commands=["start"])
dp.register_message_handler(stats_handler, commands=["stats"])
dp.register_message_handler(forall_handler, commands=["forall"])

# 📌 دستورات متنی برای افزودن و حذف ادمین
dp.register_message_handler(add_admin_handler, lambda m: m.text.startswith("افزودن ادمین "))
dp.register_message_handler(remove_admin_handler, lambda m: m.text.startswith("حذف ادمین "))

# 📌 هندلر پیام‌های متنی از طرف ادمین در حالت پاسخ‌دهی

dp.register_message_handler(
    reply_handler,
    lambda msg: get_reply(msg.from_user.id) is not None,
    content_types=types.ContentTypes.TEXT
)

# 📌 پیام کاربر در چت خصوصی

dp.register_message_handler(user_message_handler, lambda msg: msg.chat.type == "private")

# 📌 دکمه‌های پاسخ و بلاک

dp.register_callback_query_handler(admin_reply_callback, lambda c: c.data.startswith("reply"))
dp.register_callback_query_handler(block_user_callback, lambda c: c.data.startswith("block"))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
