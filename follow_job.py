import requests
from headers import get_headers
from utils import get_user_id, get_data


def follow(cookie, job_data):
    av, dtgs = get_data(cookie, job_data["link"])
    headers = get_headers(cookie, job_data["link"])
    user_id = get_user_id(cookie, job_data["link"])
    data = {
        "av": av,
        "fb_dtsg": dtgs,
        "jazoest": "26252",
        "lsd": "mL8zJl2r-SNSV1V7zEwSS0",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "useBarcelonaFollowMutationFollowMutation",
        "variables": f'{{"target_user_id":"{user_id}","container_module":"ig_text_feed_profile"}}',
        "server_timestamps": "true",
        "doc_id": "24213450504960197",
    }

    response = requests.post(
        "https://www.threads.com/graphql/query",
        headers=headers,
        data=data,
    )

    if response.status_code == 200:
        return True
    else:
        return False
