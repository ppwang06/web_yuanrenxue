"""
ja3的处理办法
为了欺骗对方，我不是同一个电脑发出的请求，而是多个
http://t.zoukankan.com/Eeyhan-p-15681207.html
"""
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
# from urllib3.util.ssl_ import create_urllib3_context
# from requests.packages.urllib3import create_urllib3_context
import requests
import random
from loguru import logger
ORIGIN_CIPHERS = ('ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
                  'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES')


class DESAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        """
        A TransportAdapter that re-enables 3DES support in Requests.
        """
        CIPHERS = ORIGIN_CIPHERS.split(':')
        random.shuffle(CIPHERS)
        CIPHERS = ':'.join(CIPHERS)
        self.CIPHERS = CIPHERS + ':!aNULL:!eNULL:!MD5'
        super().__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)


sessionid = "2tblrtmlrripa00sjsmrpo7kfk6h38bn"

headers = {
    'authority': 'match.yuanrenxue.com',
    # 使用自己的 sessionid
    'cookie': f'sessionid={sessionid}',
    'referer': 'https://match.yuanrenxue.com/match/12',
    'user-agent': 'yuanrenxue.project',
}
s = requests.Session()
s.headers.update(headers)


def get_result():
    total = 0
    for i in range(1, 6):
        params = {
            "page": str(i),
        }
        # s.mount的第一个参数表示该适配器仅在以https://ja3er.com开头的网址中生效。
        s.mount('https://match.yuanrenxue.com', DESAdapter())
        response = s.get("https://match.yuanrenxue.com/api/match/19", params=params)
        logger.info(response.json())
        # data = response.json().get("data")
        # for one in data:
        #     total += one.get("value")
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_result()

