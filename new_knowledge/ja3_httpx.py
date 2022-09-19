import httpx
import asyncio
import random
import ssl
from loguru import logger

ORIGIN_CIPHERS = ('ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
                  'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES')


class SSLFactory:
    def __init__(self):
        self.ciphers = ORIGIN_CIPHERS.split(":")

    def __call__(self) -> ssl.SSLContext:
        random.shuffle(self.ciphers)
        ciphers = ":".join(self.ciphers)
        ciphers = ciphers + ":!aNULL:!eNULL:!MD5"
        context = ssl.create_default_context()
        context.set_ciphers(ciphers)
        return context


sessionid = "2tblrtmlrripa00sjsmrpo7kfk6h38bn"

headers = {
    'authority': 'match.yuanrenxue.com',
    # 使用自己的 sessionid
    'cookie': f'sessionid={sessionid}',
    'referer': 'https://match.yuanrenxue.com/match/12',
    'user-agent': 'yuanrenxue.project',
}


def get_result():
    sslgen = SSLFactory()
    total = 0
    with httpx.Client(headers={}, http2=True, verify=sslgen()) as client:
        for i in range(1, 6):
            params = {
                "page": str(i),
            }
            response = client.get("https://match.yuanrenxue.com/api/match/19", params=params)
            logger.info(response.json())
            data = response.json().get("data")
            for one in data:
                total += one.get("value")
        logger.info(f"total:{total}")


if __name__ == '__main__':
    get_result()


