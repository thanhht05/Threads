import requests

cookies = {
    "mid": "aJxZqAALAAGH6aDpJlrgaIW4p9F7",
    "ig_did": "E60408EF-19B7-492F-A16F-51988531B928",
    "dpr": "1.25",
    "ps_l": "1",
    "ps_n": "1",
    "csrftoken": "sdUdpFjakzJEUbCfNAwFGiKH5pxoaes2",
    "ds_user_id": "76681273006",
    "sessionid": "76681273006%3AYfmky1w8Qq3XjQ%3A12%3AAYfrfltTJUt2WuIc4K58sgTXJ-gpYfMMyxuBuqTMTA",
    "rur": '"EAG\\05476681273006\\0541788322300:01fec77f1f06254de03965237a4a44bc50e04a2604e24046390403bd5d187d3b4e6e745c"',
}

headers = {
    "accept": "*/*",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.threads.com",
    "priority": "u=1, i",
    "referer": "https://www.threads.com/@tronchongsambac",
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
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "x-asbd-id": "359341",
    "x-bloks-version-id": "d11fe61c4b5ec91b034288db8827999b2ea42f4be9e4a86afe3924c302f1f830",
    "x-csrftoken": "sdUdpFjakzJEUbCfNAwFGiKH5pxoaes2",
    "x-fb-friendly-name": "useBarcelonaFollowMutationFollowMutation",
    "x-fb-lsd": "mL8zJl2r-SNSV1V7zEwSS0",
    "x-ig-app-id": "238260118697367",
    "x-root-field-name": "xdt_text_app_follow_user",
    # 'cookie': 'mid=aJxZqAALAAGH6aDpJlrgaIW4p9F7; ig_did=E60408EF-19B7-492F-A16F-51988531B928; dpr=1.25; ps_l=1; ps_n=1; csrftoken=sdUdpFjakzJEUbCfNAwFGiKH5pxoaes2; ds_user_id=76681273006; sessionid=76681273006%3AYfmky1w8Qq3XjQ%3A12%3AAYfrfltTJUt2WuIc4K58sgTXJ-gpYfMMyxuBuqTMTA; rur="EAG\\05476681273006\\0541788322300:01fec77f1f06254de03965237a4a44bc50e04a2604e24046390403bd5d187d3b4e6e745c"',
}

data = {
    "av": "17841476590195159",
    "__user": "0",
    "__a": "1",
    "__req": "3g",
    "__hs": "20333.HYP:barcelona_web_pkg.2.1...0",
    "dpr": "1",
    "__ccg": "EXCELLENT",
    "__rev": "1026574995",
    "__s": "e20atb:2e8oz5:9qrlih",
    "__hsi": "7545332197458637947",
    "__dyn": "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awgo9oO0n24oaEd82lwv89k2C1Fwc60D85m1mzXwae4UaEW0Loco5G0zK5o4q0HU420n6azo7u0zE2ZwrUdUbGw4mwr86C2q6omwxwiQ1mwLwHxW17y9UjgbVE-19xW1Vwn85SU7y",
    "__csr": "gigPsRFR5ONBiIJWZbl4nnHuOkVLBGFlDjCGaihqiyrhHhXiAUx7BUG8xiFLGHWw062SUhw-4oBgG0Yo0Lp0lUdEhUdU1fHwdK1Lg2kyod85u0JC4Xxe5k31254wPg7e483Rxm2R0Lx208Lx24A0r62S0dSw2w8fo3s1s9zJ1e2Z4d4wOy8S2W36gM9pDbxREHAG1Txda5opBgcbw8Kdw77o14Wwgawj4J0YwOAd4zA3C2W2Z770OojwJk8AgOby8F7wmU2fgoKBwoE0hX5O032o16A01OrBhrUC9g0I-1xgkBg0--09cCAw",
    "__hsdp": "gaLl8aBi0gQb8wk8z64L312hA5oApEYxxOk66dA4GgxzMijM9VYPMpcO1F6iBTqcgtg55YsFwlDxgU8m30QRPwVGdhVVdmqag28CBwAIw7e11wVBwiQ6d4xCK1yxqm2i58889k5VE2RUbo8EkwMoy13BxfUiw7Ew",
    "__hblp": "1Z04Eglx2EhwDzm8l3pE9Acg-8y8kh42q1tyUdEep8gBDxi2i68iyEf89ES4EvyEHDwIxmWUy4UqK261wwf213wqopyU4C4omBxvyAbDBxil4xZd3VGwGxW2i6u7oO8U8qxSi58jGqUpxO2l1Do1-U",
    "__sjsp": "galqQwGl813gIy1gycoiYc49a81m9eqzO6akykah2VQDzp1aA8oY4ABg9VZmUIp4My12hv8",
    "__comet_req": "29",
    "fb_dtsg": "NAftrcPrzNv9BKuzy1axbJ71D8D5bfRGtlGuLxrCohFi34Cu6y-45EA:17843669410156967:1756784307",
    "jazoest": "26252",
    "lsd": "mL8zJl2r-SNSV1V7zEwSS0",
    "__spin_r": "1026574995",
    "__spin_b": "trunk",
    "__spin_t": "1756784552",
    "__jssesw": "2",
    "__crn": "comet.threads.BarcelonaProfileThreadsColumnRoute",
    "fb_api_caller_class": "RelayModern",
    "fb_api_req_friendly_name": "useBarcelonaFollowMutationFollowMutation",
    "variables": '{"target_user_id":"63286290614","container_module":"ig_text_feed_profile"}',
    "server_timestamps": "true",
    "doc_id": "24213450504960197",
}

response = requests.post(
    "https://www.threads.com/graphql/query", cookies=cookies, headers=headers, data=data
)
with open("profile.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

# cookie = 'mid=aJxZqAALAAGH6aDpJlrgaIW4p9F7;ig_did=E60408EF-19B7-492F-A16F-51988531B928; dpr=1.25; csrftoken=jLo3teNIHGBjMksH5TuXBeIQMR02MXsd;ds_user_id=76681273006; ps_l=1; ps_n=1; sessionid=76681273006%3A4nhA6vjvbmVMvE%3A5%3AAYd7EWn_kLSNCUNylTgQWi-XdZ8eODU3CR5_6f0OmQ; rur="EAG\\05476681273006\\0541788274659:01fe963398a060dbf42e9b95d3971c0f82e0747b302a14bb33090c928e6c95ab08100ff6"'
# url = "https://www.threads.net"
# (get_data(cookie, url))
