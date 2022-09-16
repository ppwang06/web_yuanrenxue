"""
web js 逆向第十二题
使用自己的 sessionid
不使用 session_id 无法获取第四页 第五页的数据
"""
import requests
import base64
from loguru import logger

sessionid = ""


headers = {
    'authority': 'match.yuanrenxue.com',
    # 使用自己的 sessionid
    'cookie': f'sessionid={sessionid}',
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
        logger.info(response.json())
        data = response.json().get("data")
        for one in data:
            total += one.get("value")
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_result()


