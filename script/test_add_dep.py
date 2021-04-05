
import unittest  # 测试用例是在unittest框架下编写
from interface.add_department import AddDepartment
from common.get_keyword import GetKeyword
from common.operation_excel import OperationExcel
import ddt

oper = OperationExcel("../data/add_dep.xlsx") # 表格路径
test_data = oper.get_data_by_index()

@ddt.ddt
class TestAddDep(unittest.TestCase):
    def setUp(self) -> None:
        self.add_dep = AddDepartment()

    @ddt.data(*test_data)
    def test_add_dep(self, data):
        '''添加成功的测试用例'''
        re_data = {
            "data":[
                {
                    "dep_id":data["dep_id"],
                    "dep_name":data["dep_name"],
                    "master_name":data["master_name"],
                    "slogan":data["slogan"]
                }
            ]
        }
        response = self.add_dep.add_dep(re_data)  # 得到新增学院的接口返回值
        # 获取添加成功后的dep_id
        # self.add_dep.get_depid(data) # 因为直接使用该方法相当于又执行了一次添加学院接口

        if "status_code" in response.keys():  # 判断status_code是否在返回值的键中
            res = GetKeyword.get_value_by_keyword(response, "status_code")
        else:
            res = GetKeyword.get_value_by_keyword(response["create_success"], "dep_id")
        self.assertEqual(res, data["expect"])  # 断言实际获取到的dep_id和预期的dep_id做比较



        '''
        # 返回值的验证有3种情况
        # 1.添加成功
        # 2.添加id已存在的学院
        # 3.参数错误
        根据对接口文档的分析
        可以通过判断返回值是否包含“status_code"区分1,2和3，然后
        区分1,2
        根据返回值中already_exist.count是否为0，判断是否添加成功
        '''
        # 条件判断的个数，根据接口文档返回值的情况来决定
        # if "status_code" in response.key():  # 判断status_code是否在返回值的键中
        #     res = GetKeyword.get_value_by_keyword(response, "status_code")
        # else:
        #     if GetKeyword.get_value_by_keyword(response["already_exist"], "count") == 0:
        #         res = GetKeyword.get_value_by_keyword(response["create_success"], "dep_id")
        #     else:
        #         res = GetKeyword.get_value_by_keyword(response["create_success"], "dep_id")
        # expect = "预期结果"
        # self.assertEqual(res, expect)

if __name__ == '__main__':
    unittest.main()


