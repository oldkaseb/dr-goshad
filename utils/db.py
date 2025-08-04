import json
import os
from datetime import datetime

USERS_FILE = "data/users.json"
ADMINS_FILE = "data/admins.json"

# اطمینان از وجود فایل‌ها
os.makedirs("data", exist_ok=True)
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([], f)

if not os.path.exists(ADMINS_FILE):
    with open(ADMINS_FILE, "w") as f:
        json.dump([], f)

# 📦 کاربران
def get_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_user(user: dict):
    users = get_users()
    if not any(u["id"] == user["id"] for u in users):
        user["start_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        users.append(user)
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=2)

# 👮‍♂️ ادمین‌ها
def get_admins():
    with open(ADMINS_FILE, "r") as f:
        return json.load(f)

def is_admin(user_id: int):
    return user_id in get_admins()

def add_admin(user_id: int):
    admins = get_admins()
    if user_id not in admins:
        admins.append(user_id)
        with open(ADMINS_FILE, "w") as f:
            json.dump(admins, f, indent=2)

def remove_admin(user_id: int):
    admins = get_admins()
    if user_id in admins:
        admins.remove(user_id)
        with open(ADMINS_FILE, "w") as f:
            json.dump(admins, f, indent=2)
