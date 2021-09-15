import os

class Config(object):
    API_HASH = os.getenv("API_HASH")
    API_ID = int(os.getenv("API_ID"))
    HEROKU_API = os.getenv("HEROKU_API")
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
    MONGODB_URL = os.environ.get("MONGODB_URL")
    PY_SESSION = os.getenv("PYROGRAM_SESSION")
    PREFIX = os.environ.get("PREFIX", ".")
    LOG_CHAT = int(os.getenv("LOG_CHAT"))
