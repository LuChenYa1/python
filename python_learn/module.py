"""
import ... (模块名)
import 模块1, 模块2
form ...(模块名) import ...(功能名)
发现：模块不引用会变灰
起别名：后面加 as (别名)
"""

# 1、直接导入模块名
# import time
# print('你好')
# time.sleep(5)
# print('嗯，你也好')


# 2、使用form导入模块具体功能，省略模块名
# from time import sleep
# print('1')
# sleep(5)
# print('2')


# 3、使用form和*导入全部功能, 也能省略模块名，但有缺陷，容易撞名
# from time import *
# print('1')
# sleep(5)
# print('2')


# 4、as 别名
from time import sleep as sl

__all__ = ['test_a']


def test_a(x, y):
    print(x + y)


def test_b(x, y):
    print(x - y)


print('没有被放到主函数里面的非功能语句会被执行')

if __name__ == '__main__':  # 当右键运行本Python文件时，内置变量__name__会被赋值为__main__,从而进入if
    sl(5)
    print(3)
# or
# import time as t
# t.sleep(4)
