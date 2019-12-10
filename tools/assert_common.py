def assert_common(self,response,status_code=200):
    # 状态码200  默认断言状态码200,可进行传参修改
    self.assertEqual(status_code,response.status_code)
    # 断言 success
    self.assertTrue(response.json().get('success'))
    # 断言 code
    self.assertEqual(10000,response.json().get('code'))
    # 断言 message
    self.assertEqual('操作成功！',response.json().get('message'))

