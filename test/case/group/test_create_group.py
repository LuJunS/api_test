import requests
import unittest
import json
from lib.case_log import *
import os
import sys
sys.path.append("../../..")
from config.config import *
from lib.read_excel import *
from lib.case_log import log_case_info

class TestCreateGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, "test_dop_data.xlsx"), "TestCreateGroup") # 读取该测试类所有用例数据

    def test_create_Group_ture(self):
        case_data = get_test_data(self.data_list,"test_create_Group_ture") # 从数据列表中查找到该用例数据
        if not case_data: # 有可能为None
            logging.error("用例数据不存在")
        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  #需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,json=json.loads(data),headers=headers)
        log_case_info('test_create_Group_ture', url, data, expect_res, res.text)
        self.assertEqual(expect_res, res.text)


    def test_create_Group_duplication(self):
        case_data = get_test_data(self.data_list,"test_create_Group_duplication")
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data =case_data.get('data')
        expect_res = case_data.get('expect_res')
        res = requests.post(url=url, json=json.loads(data), headers=headers)
        log_case_info('test_create_Group_duplication', url, data, expect_res, res.text)
        self.assertEqual(expect_res, res.text)

    def test_delete_Group(self):
        case_data = get_test_data(self.data_list,"test_delete_Group")
        if not case_data:
            logging.error("用例数据不存在")
    



if __name__ == '__main__':
    unittest.main(verbosity=2)
