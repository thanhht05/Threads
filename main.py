import time

from config import ACCOUNT_ID
from color import GREEN, RESET, RED, BLUE, YELLOW
from threads_job import get_latest_job
from utils import check_type
from like_post import like
from follow_job import follow
from golike_api import complete_job, skip_job


def main():
    cookie = input("Nhập cookie: ")
    n = int(input("Nhập số lần muốn chạy: "))

    price = 0
    time_success = 0
    for i in range(1, n + 1):
        print(f"\n=== Lần {i}/{n} ===")
        job_data = get_latest_job()
        if not job_data:
            print("[-] Không có job để thực hiện, chờ 5 giây...")
            time.sleep(5)
            continue

        if check_type(job_data["link"]) == "POST":

            success = like(cookie, job_data)

        else:
            success = follow(cookie, job_data)

        if success:
            if complete_job(job_data):
                price += job_data["price_after_cost"]
                print(f"{BLUE}[+] Total price: {price}{RESET}")
                time_success += 1
            else:
                print(f"{RED}[!] complete_job thất bại, gửi report...")
                skip_job(job_data)
        else:
            print(f"{RED}[!] Job bị lỗi!{RESET}")
            skip_job(job_data)

        print(f"{GREEN}[+] Hoàn tất lần {time_success} / {n}{RESET}")
        print(f"[*] Đợi 5 giây trước khi job tiếp theo...", end="", flush=True)
        for j in range(10):
            print(".", end="", flush=True)
            time.sleep(1)
        print(" ✅")


if __name__ == "__main__":
    main()
