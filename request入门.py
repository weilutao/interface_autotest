# 1、导入requests库
# 2、准备接口三要素
# 2.1、请求地址
# 2.2、请求参数
# 3、发送请求

# 1
import requests
import json

# 2.1
url = "https://www.baidu.com"

# 2.2
# 没有请求参数

# 3
response = requests.get(url = url)

print(response)
# print(response.text) #将我们返回值按照文本格式显示
# print(response.json()) #将返回值以json格式显示
# print(response.status_code) #返回状态码
# print(response.headers) #返回响应头
# print(response.content) #返回响应源码

# json 和 python之间的转化
# json.dumps()  将Python转化为json字符串
# json.loads()  将json对象转化为Python
dict_json = response.json()
res = json.dumps(dict_json, indent = 2, ensure_ascii = False)
print(res)