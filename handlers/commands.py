from aiogram import types
from config import ADMIN_ID, ADMINS_FILE
from utils.database import get_users, add_admin, remove_admin, is_admin, save_user
from utils.broadcast import broadcast_message
import json
import os

# دستور ارسال پیام همگانی
async def forall_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("⛔ فقط ادمین‌ها می‌توانند از این دستور استفاده کنند.")
    await message.reply("📣 لطفاً پیام بنر همگانی را ارسال کنید.")
    # حالت ذخیره پاسخ موقت به‌صورت reply_to_all ذخیره می‌شود
    from utils.state import set_reply
    set_reply(message.from_user.id, "broadcast")

# دستور آمار کاربران
async def stats_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("⛔ فقط ادمین‌ها اجازه دسترسی دارند.")
    
    users = get_users()
    text = f"📊 آمار کلی ربات:\n\n👥 تعداد کاربران: {len(users)}\n\n"
    for user in users:
        text += f"🆔 {user['id']} | {user.get('name', '')} | @{user.get('username', '-')}\n🕒 {user.get('start_time', '')}\n\n"
    
    if len(text) > 4096:
        for x in range(0, len(text), 4096):
            await message.reply(text[x:x+4096])
    else:
        await message.reply(text)

# دستور افزودن ادمین (با پیام فارسی و آیدی عددی)
async def add_admin_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("⛔ فقط سازنده یا ادمین می‌تواند این کار را انجام دهد.")
    
    if len(message.text.split()) < 2:
        return await message.reply("❌ لطفاً آیدی عددی فرد را بعد از عبارت «افزودن ادمین» وارد کنید.")
    
    try:
        new_admin_id = int(message.text.split()[1])
    except:
        return await message.reply("❌ آیدی نامعتبر است.")
    
    add_admin(new_admin_id)
    await message.reply(f"✅ ادمین جدید با آیدی `{new_admin_id}` افزوده شد.", parse_mode="Markdown")

# دستور حذف ادمین (با پیام فارسی و آیدی عددی)
async def remove_admin_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("⛔ فقط سازنده یا ادمین می‌تواند این کار را انجام دهد.")
    
    if len(message.text.split()) < 2:
        return await message.reply("❌ لطفاً آیدی عددی فرد را بعد از عبارت «حذف ادمین» وارد کنید.")
    
    try:
        target_id = int(message.text.split()[1])
    except:
        return await message.reply("❌ آیدی نامعتبر است.")
    
    remove_admin(target_id)
    await message.reply(f"✅ ادمین با آیدی `{target_id}` حذف شد.", parse_mode="Markdown")

# دریافت پیام پس از حالت فوروارد
async def reply_handler(message: types.Message):
    from utils.state import get_reply, clear_reply
    mode = get_reply(message.from_user.id)

    if mode == "broadcast":
        clear_reply(message.from_user.id)
        users = get_users()
        await message.reply("📤 در حال ارسال پیام همگانی...")
        success, fail = await broadcast_message(users, message)
        await message.reply(f"✅ ارسال انجام شد.\n\n📬 موفق: {success} | ❌ ناموفق: {fail}")
