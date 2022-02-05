import requests

emoji_url: str = "https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u{:04d}.png"

for i in range(1, 10000):
    url: str = emoji_url.format(i)

    r = requests.get(url)
    if r.status_code == 200:
        print(f"{url} - valid")
