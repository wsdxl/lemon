# -*- coding: utf-8 -*-
# @Time      : 2019/10/18 16:21
# @Author    : XiaoLei
# @Email     : 506615839@qq.com
# @File      : base2.py
# @Software  : PyCharm

'''
Python try except finally：资源回收
如果没有 try 块，则不能有后面的 except 块和 finally 块；
except 块和 finally 块都是可选的，但 except 块和 finally 块至少出现其中之一，也可以同时出现；
可以有多个 except 块，但捕获父类异常的 except 块应该位于捕获子类异常的 except 块的后面；
不能只有 try 块，既没有 except 块，也没有 finally 块；
多个 except 块必须位于 try 块之后，finally 块必须位于所有的 except 块之后。
'''
# import os
# def test():
#     fis=None
#     try:
#         fis = open('a.txt')
#     except OSError as e:
#         print(e.strerror)
#         # return
#         os._exit(1) #在异常处理代码中使用 os.exit(1) 语句来退出 Python 解释器，则 finally 块将失去执行的机会
#     finally: #有return语句也会执行finally语句
#         # 关闭磁盘文件，回收资源
#         if fis is not None:
#             try:
#                 fis.close()
#             except OSError as ioe:
#                 print(ioe.strerror)
#         print('执行finally资源回收')
#
# test()

'''
不要在 finally 块中使用如 return 或 raise 等导致方法中止的语句,
会导致 try 块、except 块中的 return、raise 语句失效
尽量避免在 finally 块里使用 return 或 raise 等导致方法中止的语句
'''
def t():
    try:
        return True
    finally:
        return False
a=t()
print(a)








