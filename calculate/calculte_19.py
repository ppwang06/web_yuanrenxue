"""
ja3 检测
换代理 无法解决问题
pyhttpx 可以直接使用
百家号有使用这个检测
"""
import pyhttpx
from loguru import logger


sessionid = "自己session_id"


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
        }
        sess = pyhttpx.HttpSession()
        response = sess.get("https://match.yuanrenxue.com/api/match/19", headers=headers, params=params)
        logger.info(response.json)
        data = response.json.get("data")
        for one in data:
            total += one.get("value")
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_result()