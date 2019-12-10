import unittest
import api
from api.api_employee import ApiEmployee

from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.api = ApiEmployee()
    def test01_post(self,name="hxy",pwd="13934352991",num="1423229"):
        r = self.api.api_post_employee(name,pwd,num)
        print("数据:",r.json())
        api.user_id = r.json().get("data").get("id")
        print("员工id:",api.user_id)
        assert_common(self,r)

    def test02_put(self,name="hyx"):
        r = self.api.api_put_employee(name)
        print("修改的数据:",r.json())

    def test03_get(self):
        r = self.api.api_get_employee()
        print("查询到的数据:",r.json())

    def test04_delete(self):
        r = self.api.api_delete_employee()
        print("数据:",r.json())
        assert_common(self,r)
