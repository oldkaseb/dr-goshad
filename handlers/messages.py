from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID
from utils.db import is_blocked, get_admins
from utils.state import set_reply

async def user_message_handler(message: types.Message):
    if is_blocked(message.from_user.id):
        return
    text = f"📨 پیام جدید از {message.from_user.full_name} (@{message.from_user.username}):\n\n{message.text}"
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("✉️ پاسخ", callback_data=f"reply:{message.from_user.id}"),
        InlineKeyboardButton("🚫 بلاک", callback_data=f"block:{message.from_user.id}")
    )
    for admin_id in [ADMIN_ID] + get_admins():
        await message.bot.send_message(admin_id, text, reply_markup=keyboard)
    await message.reply("✉️ پیام شما ارسال شد، منتظر پاسخ بمانید.")

async def admin_reply_callback(callback_query: types.CallbackQuery):
    user_id = int(callback_query.data.split(":")[1])
    set_reply(callback_query.from_user.id, user_id)
    await callback_query.answer("حالت پاسخ‌دهی فعال شد. پیام بعدی به کاربر ارسال می‌شود.")

async def block_user_callback(callback_query: types.CallbackQuery):
    from utils.db import block_user
    user_id = int(callback_query.data.split(":")[1])
    block_user(user_id)
    await callback_query.answer("کاربر بلاک شد.")
