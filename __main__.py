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
EMOJI_URL: str = "https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u{:04d}.png"

# Checking for "emoji" folder
if not os.path.exists("emoji/"):
    os.mkdir("emoji")

# Start downloading emoji images
logger.info("Download start")
for i in range(1, 10000):
    # Generate emoji url
    url: str = EMOJI_URL.format(i)

    # Request emoji
    r = requests.get(url)

    # If emoji exists download it
    if r.status_code == 200:
        with open(f"emoji/u{i:04d}.png", "wb") as image:
            image.write(r.content)

        # Report about downloaded emoji
        logger.info(f"Emoji #{i:04d} downloaded! {9999 - i} left")
