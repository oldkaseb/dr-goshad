from aiogram import types
from config import ADMIN_ID
from utils.db import get_users, add_admin, get_admins
from utils.state import get_reply, clear_reply

async def stats_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    users = get_users()
    text = f"👥 تعداد کاربران: {len(users)}\n\n"
    for u in users:
        text += f"{u['id']} | {u['name']} | @{u['username']} | {u['start_time']}\n"
    await message.reply(text)

async def forall_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    await message.reply("✉️ لطفاً پیام همگانی را ارسال کنید.")

async def admin_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    if not message.reply_to_message:
        await message.reply("این دستور را روی پیام یک کاربر ریپلای کن.")
        return
    new_admin_id = message.reply_to_message.from_user.id
    add_admin(new_admin_id)
    await message.reply(f"✅ {new_admin_id} به لیست ادمین‌ها اضافه شد.")

async def reply_handler(message: types.Message):
    target_id = get_reply(message.from_user.id)
    if target_id:
        await message.bot.send_message(target_id, f"✉️ پاسخ ادمین:\n{message.text}")
        await message.reply("✅ پیام برای کاربر ارسال شد.")
        clear_reply(message.from_user.id)
