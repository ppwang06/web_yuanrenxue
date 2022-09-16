import httpx
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
        }
        with httpx.Client(headers=headers, http2=True) as client:
            response = client.get('https://match.yuanrenxue.com/api/match/17', params=params)
            print(response.json())
            data = response.json().get("data")
            for one in data:
                total += one.get("value")
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_result()

