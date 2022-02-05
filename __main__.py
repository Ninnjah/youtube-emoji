import os
import logging
import requests

# Config logger
logging.basicConfig(
    format="[%(asctime)s] \"%(name)s\" | %(levelname)s: %(message)s",
    datefmt="%y.%m.%d %H:%M:%S",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Emoji url template
EMOJI_URL: str = "https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u{}.png"

# Checking for "emoji" folder
if not os.path.exists("emoji/"):
    os.mkdir("emoji")

# Start downloading emoji images
logger.info("Download start")
for i in range(0x0, 0x1ffff + 1):
    # Generate hex number
    num: str = hex(i).replace("0x", "").rjust(4, "0")
    # Generate emoji url
    url: str = EMOJI_URL.format(num)

    # Request emoji
    r = requests.get(url)

    # If emoji exists download it
    if r.status_code == 200:
        with open(f"emoji/u{num}.png", "wb") as image:
            image.write(r.content)

        # Report about downloaded emoji
        logger.info(f"Emoji #{i} downloaded! {0x1ffff - i} left")

    elif r.status_code == 404:
        logger.warning(f"Emoji #{i} not exists!  {0x1ffff - i} left")

    else:
        logger.error(f"Emoji #{i} status code: {r.status_code}")
