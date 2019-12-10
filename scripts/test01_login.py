import unittest

import api

from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiLogin对象
        cls.login = ApiLogin()
    # 登录测试
    # 默认正确的参数,可进行传参修改
    def test01_login(self,mobile="13800000002",pwd="123456"):
        # 调用 ApiLogin 下的 api_login 方法
        r = self.login.api_login(mobile,pwd)
        print(r.json())
        # 提取token
        token =  r.json().get("data")
        # 给api下的headers字典进行添加,有指定key是
        api.headers["Authorization"] = "Bearer "+token
        print(api.headers)
        # 断言 调用 tools 下的assert_common
        assert_common(self,r)
