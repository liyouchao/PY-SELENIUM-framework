#在这里添加各种自定义断言，断言失败抛出异常AssertionError

def asserHTTPCode(response,code_list=None):
    res_code = response.status_code #返回的状态码
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('相应code不在列表中！')#抛出异常，unittest自动判断
