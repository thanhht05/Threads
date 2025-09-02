import random
import re
from list_user_agents import user_agents


def get_headers(cookie: str, url):
    csrftoken = re.findall(r"csrftoken=([^\s;]+)", cookie)[0]
    ua = random.choice(user_agents)
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.threads.com",
        "priority": "u=1, i",
        "referer": url,
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-full-version-list": '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.155", "Chromium";v="139.0.7258.155"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"19.0.0"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": ua,
        "x-asbd-id": "359341",
        "x-csrftoken": csrftoken,
        "x-fb-friendly-name": "useBarcelonaLikeMutationLikeMutation",
        "x-fb-lsd": "khT1eYXciEXhLhHExsEnA0",
        "x-ig-app-id": "238260118697367",
        "cookie": cookie,
    }
    return headers
