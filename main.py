from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.messages import user_message_handler, admin_reply_callback, block_user_callback
from handlers.commands import stats_handler, forall_handler, admin_handler, reply_handler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start_handler, commands=["start"])
dp.register_message_handler(stats_handler, commands=["stats"])
dp.register_message_handler(forall_handler, commands=["forall"])
dp.register_message_handler(admin_handler, commands=["admin"])
dp.register_message_handler(reply_handler, lambda msg: True, content_types=types.ContentTypes.TEXT)
dp.register_message_handler(user_message_handler, lambda msg: msg.chat.type == "private")
dp.register_callback_query_handler(admin_reply_callback, lambda c: c.data.startswith("reply"))
dp.register_callback_query_handler(block_user_callback, lambda c: c.data.startswith("block"))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
