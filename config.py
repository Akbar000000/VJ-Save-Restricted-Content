import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22188044"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "099e3a1dce52b7677299c3ab8ab3b6ca")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://akbarakbar4329:sFqcKBFqzsYobYfu@cluster0.keqgcg0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
