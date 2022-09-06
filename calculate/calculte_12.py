"""
web js 逆向第十二题
"""
import requests
import base64
from loguru import logger


headers = {
    'authority': 'match.yuanrenxue.com',
    # 使用自己的 sessionid
    'cookie': 'sessionid=obqaw4o1z00u7rllreesq2loxini0edo',
    'referer': 'https://match.yuanrenxue.com/match/12',
    'user-agent': 'yuanrenxue.project',
}


def get_result():
    total = 0
    for i in range(1, 6):
        params = {
            "page": str(i),
            "m": base64.b64encode(f"yuanrenxue{i}".encode())
        }

        response = requests.get('https://match.yuanrenxue.com/api/match/12', headers=headers, params=params)
        data = response.json().get("data")
        for one in data:
            total += one.get("value")
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_result()


