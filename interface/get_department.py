
from common.send_method import SendMethod


class GetDepartment:
    def __init__(self, method="get"):
        self.url = ""
        self.method = method

    def get_department_by_id(self, dep_id):
        '''根据指定参数，单接口测试'''
        data = {"$dep_id_list":dep_id}
        response = SendMethod.send_method(self.method, self.url, data)
        return response


