import json
import os

def load_json(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump([], f)
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def add_user(user_data):
    users = load_json("data/users.json")
    if not any(u["id"] == user_data["id"] for u in users):
        users.append(user_data)
        save_json("data/users.json", users)

def get_users():
    return load_json("data/users.json")

def is_blocked(user_id):
    return user_id in load_json("data/blocked.json")

def block_user(user_id):
    blocked = load_json("data/blocked.json")
    if user_id not in blocked:
        blocked.append(user_id)
        save_json("data/blocked.json", blocked)

def get_admins():
    return load_json("data/admins.json")

def add_admin(user_id):
    admins = get_admins()
    if user_id not in admins:
        admins.append(user_id)
        save_json("data/admins.json", admins)
