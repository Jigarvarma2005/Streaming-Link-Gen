import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
import time
from config import Config
import pyrogram
import pyromod.listen
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

if __name__ == "__main__" :
    app.run()