import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your db channel ID (if applicable)
# CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

"""Retrieves channel IDs from the environment variable."""
channel_ids_str = os.environ.get("CHANNEL_ID", "")
CHANNEL_ID = [-1001729892476, -1002209106676]  # Default channel IDs

for channel_id_str in channel_ids_str.split(","):
    try:
        CHANNEL_ID.append(int(channel_id_str.strip()))
    except ValueError:
        print(f"Invalid channel ID: {channel_id_str}")

# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

# Port
PORT = os.environ.get("PORT", "8080")

# Database (if applicable)
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Force sub channel ID (optional)
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hi  {first}\n\nI am private files store bot for @animedualaudiozippercartoonist Channel. Join All Channels then try again bot will send you files if you have any problem ask in main channel")

# Admins list
ADMINS = []
try:
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join all channels Channel</b>")

# Custom caption (optional)
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Protect content (optional)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Disable channel button sharing (optional)
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.
