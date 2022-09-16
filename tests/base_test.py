import requests

headers = {
    'authority': 'match.yuanrenxue.com',
    'cookie': 'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1661310965,1662434430; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1662434463,1662450345,1662450360,1663311165; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1662434573,1662450348,1662450384,1663311165; qpfccr=true; no-alert3=true; tk=-5786214026652788959; sessionid=bc0uum112whuzk6z7xx7nfi4k4g1sn27; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1663311654; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1663311738',
    'referer': 'https://match.yuanrenxue.com/match/19',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
params = {
    "page": 3
}
response = requests.get('https://match.yuanrenxue.com/api/match/19', headers=headers, params=params)
print(response.text)


# 过ja3 反爬手段
import pyhttpx
sess = pyhttpx.HttpSession()
url = "https://match.yuanrenxue.com/api/match/19?page=1"
response = sess.get(url)
print(response.text)

