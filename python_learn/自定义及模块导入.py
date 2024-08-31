"""
注意，当导入的两个模块中存在同名函数、变量、类
同时使用会让后面导入的模块覆盖前面的模块
还有，导入整个模块会使该模块内的非主函数内容被执行，所以不建议在模块内写除函数、变量、类以外的东西
要测试函数、类的功能的话，建议写在模块的主函数内，防止被执行
__all__变量，在使用*引用模块全部功能时，限制引用功能的范围,只能使用all所框定的功能
"""

# import module
from module import *

import my_utils.file_utils
from my_utils.str_utils import *


if __name__ == '__main__':
    test_a(4, 5)
#     即使导入模块所有内容，test_b()函数也无法引用，因为模块的__all__列表变量限定了‘test_a’
# 但__all__只针对*,正常用具体函数名字导入是可以的

# 模块下载 pip install numpy
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
# 清华源

    con1 = str_reverse('史蒂夫归还借款')
    con2 = substr('水电费规划局可', 5, 8)
    print(con1)
    print(con2)
    my_utils.file_utils.append_to_file('D:/123.txt', '岁的法国')
    my_utils.file_utils.print_file_info('D:/123.txt')

