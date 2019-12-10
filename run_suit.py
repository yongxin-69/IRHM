# 导包
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
# 定义测试套件
suite=unittest.defaultTestLoader.discover("./scripts")
# 获取报告存储位置,实例化HTMLTestRunner     调用run
with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)









