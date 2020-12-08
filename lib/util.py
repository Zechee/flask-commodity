# from functools import wraps
# def max_res(a_func):
#     @wraps(a_func)
#     def return_res():
#         max_res_d(a_func())
#     return return_res()


# def max_res_d(result,code='200',message=None):
def max_res(result, code=200):
    return ({'code': code, 'data': result}, code)

def max_err(errmsg=None, code=200):
    res = {'code': code, 'msg': errmsg}
    return (res, code)