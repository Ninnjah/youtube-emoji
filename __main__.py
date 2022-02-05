import logging
import requests

logger = logging.getLogger(__name__)

emoji_url: str = "https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u{:04d}.png"

for i in range(1, 10000):
    url: str = emoji_url.format(i)

    r = requests.get(url)
    if r.status_code == 200:
        with open(f"u{i:04d}.png", "wb") as image:
            image.write(r.content)

        logger.info(f"Emoji #{i:04d} downloaded! {9999 - i} left")
