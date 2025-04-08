# encoding:utf-8
import requests

# 接口地址
url = "https://api.map.baidu.com/location/ip"

# 此处填写你在控制台-应用管理-创建应用后获取的AK
ak = "N9k2Q0OCY62Ao9FHlLyfGcGZ94Fq3aaP"

params = {
    # "ip":    "111.206.214.37",
    # "coor":    "bd09ll",
    "ak":       ak,

}

response = requests.get(url=url, params=params)
if response:
    print(response.json())