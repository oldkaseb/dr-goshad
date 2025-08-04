### ✅ فایل نهایی: utils/state.py

reply_states = {}  # user_id: target_user_id

def set_reply(admin_id: int, target_id: int):
    reply_states[admin_id] = target_id

def get_reply(admin_id: int):
    return reply_states.get(admin_id)

def clear_reply(admin_id: int):
    reply_states.pop(admin_id, None)
