from aiogram import types
from config import ADMIN_ID
from utils.db import get_users, add_admin, get_admins, is_blocked, save_json
from utils.state import get_reply, clear_reply

# حافظه موقتی برای حالت ارسال همگانی
broadcast_waiting = {}

async def stats_handler(message: types.Message):
    if message.from_user.id not in [ADMIN_ID] + get_admins():
        return

    users = get_users()
    if not users:
        await message.reply("هیچ کاربری ثبت نشده.")
        return

    text = f"👥 تعداد کاربران: {len(users)}\n\n"
    for u in users:
        text += (
            f"🆔 {u['id']} | 👤 {u['name']} | "
            f"@{u['username']} | ⏱ {u['start_time']}\n"
        )

    await message.reply(text)

async def forall_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    broadcast_waiting[message.from_user.id] = True
    await message.reply("✉️ لطفاً پیام همگانی را ارسال کنید (متنی یا تصویری).")

async def handle_broadcast_content(message: types.Message):
    if not broadcast_waiting.get(message.from_user.id):
        return

    users = get_users()
    count = 0
    for user in users:
        if not is_blocked(user["id"]):
            try:
                await message.copy_to(user["id"])
                count += 1
            except:
                pass

    await message.reply(f"✅ پیام همگانی برای {count} کاربر ارسال شد.")
    broadcast_waiting.pop(message.from_user.id, None)

async def add_admin_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    if not message.text.startswith("افزودن ادمین "):
        return

    parts = message.text.split()
    if len(parts) != 3 or not parts[2].isdigit():
        await message.reply("❗️ لطفاً دستور را به‌صورت زیر وارد کنید:\nافزودن ادمین 1234567890")
        return

    new_admin_id = int(parts[2])
    add_admin(new_admin_id)
    await message.reply(f"✅ ادمین با آیدی {new_admin_id} افزوده شد.")

async def remove_admin_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    if not message.text.startswith("حذف ادمین "):
        return

    parts = message.text.split()
    if len(parts) != 3 or not parts[2].isdigit():
        await message.reply("❗️ لطفاً دستور را به‌صورت زیر وارد کنید:\nحذف ادمین 1234567890")
        return

    target_id = int(parts[2])
    admins = get_admins()

    if target_id not in admins:
        await message.reply("⚠️ این آیدی جزو ادمین‌ها نیست.")
        return

    admins.remove(target_id)
    save_json("data/admins.json", admins)
    await message.reply(f"❌ ادمین با آیدی {target_id} حذف شد.")

async def reply_handler(message: types.Message):
    target_id = get_reply(message.from_user.id)
    if not target_id:
        return

    try:
        await message.bot.send_message(
            target_id,
            f"✉️ پاسخ ادمین:\n{message.text}"
        )
        await message.reply("✅ پیام برای کاربر ارسال شد.")
    except Exception as e:
        await message.reply(f"❌ خطا در ارسال پیام:\n{e}")
    finally:
        clear_reply(message.from_user.id)
