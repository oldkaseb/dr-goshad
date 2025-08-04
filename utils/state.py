from collections import defaultdict

# وضعیت پاسخ‌دهی ادمین‌ها به کاربران
# کلید: admin_id، مقدار: user_id
reply_targets = defaultdict(int)

def set_reply(admin_id, user_id):
    """ادمین وارد حالت پاسخ‌دهی به یک کاربر می‌شود"""
    reply_targets[admin_id] = user_id

def get_reply(admin_id):
    """بررسی اینکه آیا ادمین در حالت پاسخ‌دهی هست یا نه"""
    return reply_targets.get(admin_id)

def clear_reply(admin_id):
    """خروج ادمین از حالت پاسخ‌دهی پس از ارسال پاسخ"""
    reply_targets.pop(admin_id, None)
