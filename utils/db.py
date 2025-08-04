### ✅ فایل نهایی: utils/db.py

import json
import os
from config import USERS_FILE, ADMINS_FILE

# ذخیره اطلاعات کاربر جدید

def save_user(user_id, full_name, username):
    users = load_users()
    if user_id not in users:
        users[user_id] = {
            "full_name": full_name,
            "username": username,
            "start_time": __import__('datetime').datetime.now().isoformat()
        }
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

# بارگذاری همه کاربران

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, encoding="utf-8") as f:
        return json.load(f)

def get_users():
    return load_users()

# ادمین‌ها

def load_admins():
    if not os.path.exists(ADMINS_FILE):
        return []
    with open(ADMINS_FILE, encoding="utf-8") as f:
        return json.load(f)

def save_admins(admins):
    with open(ADMINS_FILE, "w", encoding="utf-8") as f:
        json.dump(admins, f, ensure_ascii=False, indent=2)

def is_admin(user_id):
    return int(user_id) in load_admins()

def add_admin(user_id):
    admins = load_admins()
    if int(user_id) not in admins:
        admins.append(int(user_id))
        save_admins(admins)

def remove_admin(user_id):
    admins = load_admins()
    if int(user_id) in admins:
        admins.remove(int(user_id))
        save_admins(admins)
