import time
import requests

from headers import get_headers
from utils import get_post_id, get_data


def like(cookie: str, job_data):
    post_id = get_post_id(cookie, job_data["link"])
    av, dtgs = get_data(cookie, job_data["link"])
    headers = get_headers(cookie, job_data["link"])
    data = {
        "av": av,
        "fb_dtsg": dtgs,
        "jazoest": "26228",
        "lsd": "khT1eYXciEXhLhHExsEnA0",
        "__spin_r": "1026562073",
        "__spin_b": "trunk",
        "__spin_t": "1756738349",
        "__crn": "comet.threads.BarcelonaPostColumnRoute",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "useBarcelonaLikeMutationLikeMutation",
        "variables": f'{{"mediaID":"{post_id}"}}',
        "server_timestamps": "true",
        "doc_id": "9558134877619484",
    }
    print("Sau 5s sẽ like")
    for j in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print()
    response = requests.post(
        "https://www.threads.com/api/graphql",
        headers=headers,
        data=data,
    )

    if response.status_code == 200:
        return True
    else:
        return False
