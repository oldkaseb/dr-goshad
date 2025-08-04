from aiogram import types

welcome_text = (
    "سلام!\n"
    "به ربات دکتر گشاد خوش اومدی 🌟\n\n"
    "میتونی درخواستت رو همینجا ارسال کنی گشادم ولی دارم سعی میکنم جواب همه رو بدم."
)

async def start_handler(message: types.Message):
    await message.reply(welcome_text)
