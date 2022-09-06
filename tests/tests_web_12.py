"""
第12题测试
btoa('yuanrenxue' + window.page)
"""
import requests

headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'sessionid=obqaw4o1z00u7rllreesq2loxini0edo',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/12',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'yuanrenxue.project',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('page', '1'),
    ('m', 'eXVhbnJlbnh1ZTE='),
)

response = requests.get('https://match.yuanrenxue.com/api/match/12', headers=headers, params=params)
print(response.text)
