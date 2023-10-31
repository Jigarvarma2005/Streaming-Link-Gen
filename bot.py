import logging
import os
import time
from config import Config
import pyrogram
import wget
import pyromod.listen

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
botStartTime = time.time()

# create download directory, if not exist
if not os.path.isdir(Config.DOWNLOAD_LOCATION):
    os.makedirs(Config.DOWNLOAD_LOCATION)
plugins = dict(
    root="plugins"
)

app = pyrogram.Client(
    "StreamingLinkRobot",
    bot_token=Config.TG_BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)


def BootUpProcess() -> bool:
    token_pickle = "token.pickle"
    if Config.TOKEN_PICKLE:
        token_pickle = wget.download(Config.TOKEN_PICKLE, out=token_pickle)
    if not os.path.exists(token_pickle):
        print("token.pickle file not found!")
        return False
    return True


if __name__ == "__main__":
    print("Starting ...")
    if success := BootUpProcess():
        app.start()
        print("\nBot Started!\n")
        pyrogram.idle()
        app.stop()
    print("Exiting ...")
