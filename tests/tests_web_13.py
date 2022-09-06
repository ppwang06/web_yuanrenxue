"""
web端  第13题
"""
import re
import requests
from loguru import logger


def get_web_ck():
    headers = {
        'authority': 'match.yuanrenxue.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'sessionid=自己的sessionid',
        'pragma': 'no-cache',
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
        'cookie': f'sessionid=自己的sessionid;{ck}',
        'referer': 'https://match.yuanrenxue.com/match/13',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    params = {
        "page": "2"
    }
    response = requests.get('https://match.yuanrenxue.com/api/match/13', headers=headers, params=params)
    print(response.text)


if __name__ == '__main__':
    get_data()








