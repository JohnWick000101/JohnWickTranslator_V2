from pyrogram import Client
import os

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
token = os.environ["TOKEN"]

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=token,
        api_hash=api_hash,
        api_id=api_id,
        plugins=plugins
    )
    app.run()
