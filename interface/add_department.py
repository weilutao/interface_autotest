

from common.send_method import SendMethod
from common.get_keyword import GetKeyword

class AddDepartment:
    def __init__(self, method="post"):
        self.url = ""
        self.method = method

    def add_dep(self, data):
        '''请求新增接口,针对单接口测试'''
        response = SendMethod.send_method(self.method, self.url, data)
        return response

    def get_depid(self, data):
        '''
        获取dep_id，为关联接口测试准备
        :param data: 接口返回值
        :return: dep_id
        '''
        response = self.add_dep(data)
        #获取dep_id
        dep_id = GetKeyword.get_value_by_keyword(response, "dep_id")
        
        return dep_id