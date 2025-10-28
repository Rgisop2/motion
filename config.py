from os import environ

API_ID = int(environ.get("API_ID", "28862088"))
API_HASH = environ.get("API_HASH", "47c26d543b17d010573fd34a4c3732dd")
BOT_TOKEN = environ.get("BOT_TOKEN", "7892962498:AAENGob8a3-UuoRZgLVqOScEscn5q4jUnOg")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002073865889"))
ADMINS = int(environ.get("ADMINS", "1327021082"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://Takiusername02:Takiusername02@cluster0.zo4sa5k.mongodb.net/?appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjlinkchangerbot")
