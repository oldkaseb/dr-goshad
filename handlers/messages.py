from aiogram import types
from utils.db import add_user, is_admin, get_admins, is_blocked
from utils.state import get_reply, set_reply, clear_reply

# دریافت پیام کاربر
async def user_message_handler(message: types.Message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
    if is_blocked(user_id):
        return await message.reply("\u274c شما مسدود شده‌اید.")

    add_user(user_id, message.from_user.full_name, message.from_user.username or "-")

    for admin_id in get_admins():
        try:
            await message.bot.send_message(
                admin_id,
                f"\u2709\ufe0f پیام جدید از [{message.from_user.full_name}](tg://user?id={user_id}):\n\n{message.text}",
                parse_mode="Markdown",
                reply_markup=types.InlineKeyboardMarkup().add(
                    types.InlineKeyboardButton("\u2709\ufe0f پاسخ", callback_data=f"reply:{user_id}"),
                    types.InlineKeyboardButton("\u274c بلاک", callback_data=f"block:{user_id}")
                )
            )
        except:
            pass
    await message.reply("\u2705 پیام شما برای پشتیبانی ارسال شد.")

# پاسخ دادن از دکمه
async def admin_reply_callback(callback: types.CallbackQuery):
    admin_id = callback.from_user.id
    if not is_admin(admin_id):
        return
    user_id = int(callback.data.split(":")[1])
    set_reply(admin_id, user_id)
    await callback.message.reply("\u2709\ufe0f لطفاً پاسخ خود را برای کاربر ارسال کنید.")
    await callback.answer()

# بلاک کردن کاربر
async def block_user_callback(callback: types.CallbackQuery):
    admin_id = callback.from_user.id
    if not is_admin(admin_id):
        return
    user_id = int(callback.data.split(":")[1])
    from utils.db import block_user
    block_user(user_id)
    await callback.message.reply("\u274c کاربر بلاک شد.")
    await callback.answer()
