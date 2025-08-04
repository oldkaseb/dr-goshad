### ✅ فایل کامل و نهایی: main.py

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.messages import user_message_handler, admin_reply_callback, block_user_callback
from handlers.commands import stats_handler, forall_handler, add_admin_handler, remove_admin_handler, reply_handler
from utils.state import get_reply

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ثبت دستورات
dp.register_message_handler(start_handler, commands=["start"])
dp.register_message_handler(stats_handler, lambda m: m.text.lower().startswith("آمار"))
dp.register_message_handler(forall_handler, lambda m: m.text.lower().startswith("پیام همگانی"))
dp.register_message_handler(add_admin_handler, lambda m: m.text.lower().startswith("افزودن ادمین"))
dp.register_message_handler(remove_admin_handler, lambda m: m.text.lower().startswith("حذف ادمین"))

# هندل پیام پاسخ ادمین
@dp.message_handler(lambda m: get_reply(m.from_user.id) is not None, content_types=types.ContentTypes.TEXT)
async def handle_admin_reply(message: types.Message):
    await reply_handler(message)

# فقط پیام کاربران در چت خصوصی
dp.register_message_handler(user_message_handler, lambda msg: msg.chat.type == "private")

# کال‌بک‌ها
dp.register_callback_query_handler(admin_reply_callback, lambda c: c.data.startswith("reply"))
dp.register_callback_query_handler(block_user_callback, lambda c: c.data.startswith("block"))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
