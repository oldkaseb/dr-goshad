from collections import defaultdict

reply_targets = defaultdict(int)

def set_reply(admin_id, user_id):
    reply_targets[admin_id] = user_id

def get_reply(admin_id):
    return reply_targets.get(admin_id)

def clear_reply(admin_id):
    reply_targets.pop(admin_id, None)
