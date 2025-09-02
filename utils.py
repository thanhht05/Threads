import re
import requests
from headers import get_headers


def check_type(url):
    if "/post/" in url:
        return "POST"
    else:
        return "PROFILE"


def write_file(url, response):
    if check_type(url) == "POST":
        with open("post.txt", "w", encoding="utf-8") as f:
            f.write(response)
    else:
        with open("profile.txt", "w", encoding="utf-8") as f:
            f.write(response)


def get_post_id(cookie: str, url):
    headers = get_headers(cookie, url)
    response = requests.get(url, headers=headers).text
    write_file(url, response)
    with open("post.txt", "r", encoding="utf-8") as f:
        content = f.read()

    matches = re.findall(r'"post_id":"(\d+)"', content)

    if not matches:
        return None
    return str(matches[0])


def get_data(cookie: str, url):
    with open("post.txt", "r", encoding="utf-8") as f:
        content = f.read()
    try:
        av = re.findall(r'"actorID":"(\d+)', content)[0]
        dtsg = re.findall(r'"f":"([^"]+)"', content)[0]
        print("av:", av)
        print("dtsg:", dtsg)
    except Exception as e:
        print("Lỗi khi lấy av, dtsg:", e)
        av, dtsg = None, None

    return av, dtsg


def get_user_id(cookie: str, url):
    headers = get_headers(cookie, url)
    respone = requests.get(url, headers=headers).text
    write_file(url, respone)
    with open("profile.txt", "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r'"user_id":"(\d+)"', content)
    if not matches:
        return None
    return str(matches[0])
