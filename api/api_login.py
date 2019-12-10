# 导包
import api
import requests

class ApiLogin:
    # 初始化
    def __init__(self):
        # 初始化url
        self.url = api.BASE_URL+"/api/sys/login"
    def api_login(self,mobile,pwd):
        # 创建请求数据
        data = {"mobile":mobile,"password":pwd}
        # 返回响应对象
        return requests.post(url=self.url,json=data,headers=api.headers)



