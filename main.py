from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.messages import user_message_handler, admin_reply_callback, block_user_callback
from handlers.commands import (
    stats_handler,
    forall_handler,
    handle_broadcast_content,
    reply_handler,
    add_admin_handler,
    remove_admin_handler
)
from utils.state import get_reply

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# دستورات فارسی برای افزودن و حذف ادمین
dp.register_message_handler(add_admin_handler, lambda msg: msg.text.startswith("افزودن ادمین"))
dp.register_message_handler(remove_admin_handler, lambda msg: msg.text.startswith("حذف ادمین"))

# آمار و ارسال همگانی
dp.register_message_handler(stats_handler, commands=["stats"])
dp.register_message_handler(forall_handler, commands=["forall"])
dp.register_message_handler(handle_broadcast_content, content_types=types.ContentTypes.ANY)

# فقط اگر ادمین در حالت پاسخ باشد، پیام بعدی را به کاربر بفرستد
dp.register_message_handler(
    reply_handler,
    lambda msg: get_reply(msg.from_user.id) is not None,
    content_types=types.ContentTypes.TEXT
)

# دریافت پیام از کاربر (فقط در چت خصوصی)
dp.register_message_handler(
    user_message_handler,
    lambda msg: msg.chat.type == "private"
)

# دکمه‌های پاسخ و بلاک
dp.register_callback_query_handler(admin_reply_callback, lambda c: c.data.startswith("reply"))
dp.register_callback_query_handler(block_user_callback, lambda c: c.data.startswith("block"))

if __name__ == "__main__":
    print("✅ ربات با موفقیت راه‌اندازی شد.")
    executor.start_polling(dp, skip_updates=True)
