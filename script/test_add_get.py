# 测试添加和查询关联接口

import unittest
from interface.add_department import AddDepartment
from interface.get_department import GetDepartment
from common.get_keyword import GetKeyword

class TestAddGet(unittest.TestCase):
    def setUp(self) -> None:
        self.add_dep = AddDepartment()  # 实例化添加
        self.get_dep = GetDepartment()  # 实例化查询

    def test_add_get(self):
        # 添加接口的请求参数
        add_data = {
            "data": [
                {
                    "dep_id": "T01",
                    "dep_name": "Test",
                    "master_name": "Test-M",
                    "slogan": "Here is slogan"
                }
            ]
        }
        # 执行添加接口  目的：获取添加成功后的id
        dep_id = self.add_dep.get_depid(add_data)
        # 执行查询接口
        get_res = self.get_dep.get_department_by_id(dep_id)
        # 获取查询后的id
        get_depid = GetKeyword.get_value_by_keyword(get_res, "dep_id")
        self.assertEqual(get_depid, dep_id)


