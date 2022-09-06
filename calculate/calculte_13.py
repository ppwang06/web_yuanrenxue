from loguru import logger
import requests
import re


sessionid = "自己的sessionid"


def get_web_ck():
    headers = {
        'authority': 'match.yuanrenxue.com',
        'cookie': f'sessionid={sessionid}',
        'referer': 'https://match.yuanrenxue.com/match/13',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^104^\\^, ^\\^',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    response = requests.get('https://match.yuanrenxue.com/match/13', headers=headers)
    cookie = re.search(r"document.cookie=(.*?)\+\';path=", response.text).group(1)
    end_cookie = "".join(re.findall(r"\'(.*?)\'", cookie))
    return end_cookie


def get_data():
    ck = get_web_ck()
    logger.info(f"ck:{ck}")
    headers = {
        'authority': 'match.yuanrenxue.com',
        'cookie': f'sessionid={sessionid};{ck}',
        'referer': 'https://match.yuanrenxue.com/match/13',
        'user-agent': 'yuanrenxue.project',
    }
    total = 0
    for i in range(1, 6):
        params = {
            "page": str(i),
        }
        response = requests.get('https://match.yuanrenxue.com/api/match/13', headers=headers, params=params)
        data = response.json().get("data")
        for one in data:
            total += one.get("value")
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_data()


