import api
import requests




class ApiEmployee:
    # 初始化
    def __init__(self):
        # 初始化url
        self.url_add = api.BASE_URL+"/api/sys/user"
        # {}为占位符,传入员工id
        self.url_delete = api.BASE_URL + "/api/sys/user/{}"

    #  添加员工
    def api_post_employee(self,name,pwd,num):
        # 创建json数据
        data ={"username": name,"mobile": pwd,"workNumber": num}
        # 调用post方法,必须return(返回)
        return requests.post(url=self.url_add,json=data,headers=api.headers)
    # 修改
    def api_put_employee(self,name):
        data={"username":name}
        return requests.put(url=self.url_delete.format(api.user_id), json=data, headers=api.headers)
    # 查询
    def api_get_employee(self):
        return requests.get(url=self.url_delete.format(api.user_id), headers=api.headers)

    # 删除
    def api_delete_employee(self):
        # user_id 为添加后员工的id
        return requests.delete(url=self.url_delete.format(api.user_id),headers=api.headers)



