import json
import os

DB_FILE = "database.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"users": {}, "admins": []}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)

def get_users():
    return load_db().get("users", {})

def get_admins():
    return load_db().get("admins", [])

def is_admin(user_id):
    return user_id in get_admins()

def add_admin(user_id):
    db = load_db()
    if user_id not in db["admins"]:
        db["admins"].append(user_id)
        save_db(db)

def remove_admin(user_id):
    db = load_db()
    if user_id in db["admins"]:
        db["admins"].remove(user_id)
        save_db(db)

def add_user(user_id, name, username):
    db = load_db()
    db["users"][str(user_id)] = {"name": name, "username": username}
    save_db(db)

def is_blocked(user_id):
    db = load_db()
    return str(user_id) in db.get("blocked", [])

def block_user(user_id):
    db = load_db()
    if "blocked" not in db:
        db["blocked"] = []
    db["blocked"].append(str(user_id))
    save_db(db)
