"""
第16题  该题魔改了md5的方法
-67217
"""
import random
import time
import execjs
import requests
from loguru import logger


sessionid = "自己session_id"


headers = {
    'authority': 'match.yuanrenxue.com',
    # 使用自己的 sessionid
    'cookie': f'sessionid={sessionid}',
    'referer': 'https://match.yuanrenxue.com/match/12',
    'user-agent': 'yuanrenxue.project',
}


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def get_m(e):
    base_str = "U9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi+9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi"
    c = []
    o, a, s, ll = 0, 0, 0, 0
    while True:
        if ll >= len(e):
            break
        a = ord(e[ll])
        s = ll % 6
        if s == 0:
            index = int_overflow(a >> 2)
            c.append(base_str[index])
        if s == 1:
            index = int_overflow((2 & o) << 3) | int_overflow(a >> 4)
            c.append(base_str[index])
        if s == 2:
            index = int_overflow((15 & o) << 2) | int_overflow(a >> 6)
            c.append(base_str[index])
            index = a & 63
            c.append(base_str[index])
        if s == 3:
            index = int_overflow(a >> 3)
            c.append(base_str[index])
        if s == 4:
            index = int_overflow((4 & o) << 6) | int_overflow(a >> 6)
            if index > len(base_str):
                c.append("")
            else:
                c.append(base_str[index])
        if s == 5:
            index = int_overflow((o & 15) << 4) | int_overflow(a >> 8)
            c.append(base_str[index])
            index = a & 63
            c.append(base_str[index])
        o = a
        ll += 1
    index = int_overflow((o & 3) << 4)
    c.append(base_str[index])
    c.append("FM")
    res_str = "".join(c)

    with open("../js/cal16.js", 'r', encoding='UTF-8') as f:
        js_code = f.read()
    context = execjs.compile(js_code)
    result = context.call("md5_magic_change", res_str)
    start = "".join(random.sample("ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", 15))
    end = "".join(random.sample("ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", 10))
    end_res = start + result + end
    return end_res


def get_result():
    total = 0
    for i in range(1, 6):
        t = int(time.time()) * 1000
        m = get_m(str(t))
        params = (
            ('page', i),
            ('m', m),
            ('t', t),
        )

        response = requests.get('https://match.yuanrenxue.com/api/match/16', headers=headers, params=params)
        logger.info(response.text)
        data = response.json().get("data")
        for one in data:
            total += one.get("value")
    logger.info(f"total:{total}")


if __name__ == '__main__':
    # print(int(time.time()))
    # get_m("1663576994000")
    # get_m("1663577370000")
    get_result()


