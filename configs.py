# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "TheRename_Robot")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 1478357602)
    CAPTION = "**© @TheRename_Robot**"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "David_Botz")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://David12345:David12345@cluster0.ol6px.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """ I Am Rename Bot
    """
    PROGRESS = """
⭕ **Percentage** : {0}%
⭕ **Done** : {1}
⭕ **Total** : {2}
⭕ **Speed** : {3}/s
⭕ **Time Status** : {4}
    """
