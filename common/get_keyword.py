'''
get_keyword.py
    在接口返回值中，通过关键字获取对应值
1、需要安装一个库： jsonpath
    pip install jsonpath
2、 jsonpath的使用
    jsonpath.jsonpath(数据源, jsonpath表达式)
        jsonpath表达式:$..关键字
'''
# 1、导入jsonpath库
import jsonpath
# 2、数据源
# data = {}
# 3、根据关键字查找对应值
# print(jsonpath.jsonpath(data, "$..dep_id"))


# 封装
class GetKeyword:
    @staticmethod
    def get_value_by_keyword(data, keyword):
        '''
        通过关键字，获取对应的值，
        只获取一个，如果有多个，获取第一个
        :param data: 数据源（接口返回值）
        :param keyword: 关键字
        :return: 关键字对应的值
        '''
        return jsonpath.jsonpath(data, f"$..{keyword}")[0]

    @staticmethod
    def get_values_by_keyword(data, keyword):
        '''
        通过关键字，获取对应的一组数据
        :param data: 数据源（接口返回值）
        :param keyword: 关键字
        :return: 关键字对应的值
        '''
        return jsonpath.jsonpath(data, f"$..{keyword}")


if __name__ == '__main__':
    data = None
    print(GetKeyword.get_value_by_keyword(data, "keyword"))