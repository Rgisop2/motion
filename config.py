from os import environ

API_ID = int(environ.get("API_ID", "6643753"))
API_HASH = environ.get("API_HASH", "88dfedc7b743512395bbd5153b201102")
BOT_TOKEN = environ.get("BOT_TOKEN", "8477280257:AAF5DCqXv4GtP0GhwlsQcplYChGYYDcbVRE")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002073865889"))
ADMINS = int(environ.get("ADMINS", "1327021082"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://Takiusername05:Takiusername05@cluster0.8fv3tnw.mongodb.net/?appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjlinkchangerbot")
