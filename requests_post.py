# （1） 请求正文是application/x-www-form-urlencoded

import requests
import json

# url = "http://httpbin.org/post"
# data = {
#     "userid":"admin",
#     "pwd":"123456",
#     "date":"20200312"
# }
# response = requests.post(url=url, data=data)
#
# print(response.text)


# （2） 请求正文是multipart/form-data
from requests_toolbelt import MultipartEncoder

url1 = "https://httpbin.org/post"
data = {
"userid":"admin",
    "pwd":"123456",
    "date":"20200312"
}

# 重新组合header
m = MultipartEncoder(fields=data)
headers = {
    "contentType":m.content_type
}

response1 = requests.post(url=url1, data=data, headers=headers, verify=False)
print(response1.text)

# （3） 请求正文是raw

url2 = "https://bellonlinetest.bell.ai/online/v1/user/api/login"

json1 = {
    "mobile": "18312840013",
    "captcha": "205481",
    "client": "s_pc"
}

response2 = requests.post(url=url2, json=json1)
res = json.dumps(response2.json(), indent=2, ensure_ascii=False)

print(res)


#（4） 请求正文是binary

url3 = "https://httpbin.org/post"

files = open("test.txt","rb")
data = {"file":files}

response3 = requests.post(url=url3, files=data, verify=False)
print(response3.text)
