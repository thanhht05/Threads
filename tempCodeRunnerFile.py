def get_data(cookie: str, url):
    with open("out.txt", "r", encoding="utf-8") as f:
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
