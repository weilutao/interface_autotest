import requests
import json

# 获取手机验证码
url = "https://bellonlinetest.bell.ai/online/v1/user/api/sms_captcha_send"
params = {"mobile":"13049168724"}

response = requests.get(url=url, params = params)
res = json.dumps(response.json(), indent=2, ensure_ascii=False)

print(res)
print(response)