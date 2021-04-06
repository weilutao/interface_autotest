'''
1.封装接口请求方式-----依据接口文档，不同的项目，send_method也不太一样
2.封装思路----结合接口三要素
    请求地址+请求方式
    请求参数
    返回值
3.实例
    结合接口文档，封装send_method
'''

import requests
import json

class SendMethod():
    '''
    请求方式：get,post,put, delete
    请求参数：
        get,delete:params
        post,put:json
    返回值类型：json
    '''
    @staticmethod # 静态方法不需要实例化，使用方式：类名.静态方法
    def send_method(method, url, params=None, json=None):
        if method == 'get' or method == 'delete':
            requests.request(method=method, url=url, params=params)
        elif method == 'post' or method == 'put':
            requests.request(method=method, url=url, json=json)
        else:
            print('请求方式不正确')
            response = None
        if method == 'delete':
            return response.status_code  # 如果请求方式是delete，只返回状态码
        else:
            return response.json()

    @staticmethod
    def format_response(response):
        '''
        格式化返回数据
        :param response: 返回数据
        :return: 返回美化后的json格式数据
        '''
        return json.dumps(response, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    url ='....'
    method = 'get'
    params = {"canshu":"zhi"}
    res = SendMethod.send_method(method=method, url=url, params=params)
    print(SendMethod.format_response(res))