"""
函数可返回多个值，不用打括号，用逗号分隔
实际参数类型：位置参数、关键字参数、缺省参数
函数出现多个形参时，其位置顺序是：位置参数、关键字参数、缺省参数
形参赋值没有空格
这里有一个注意点：不建议变量、函数之类的重名，会有警告
"""


def test_return():
    return 1, True, "Python"


x, y, z = test_return()
print(x, type(x), y, type(y), z, type(z))


def user_info(name, age, gender='男'):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")


# 位置参数 —— 默认使用形式
user_info("小天", 15, '女')
user_info(13, 12, '女')  # 该句说明形参没有数据类型限制

# 关键字参数
user_info('小王', age=16, gender='男')
user_info(name='小王', gender='女', age=16)  # 该句说明关键字参数可变换位置

# 缺省参数 —— 可以省略，可以另外赋值，另两种不行,位置一般在最后
user_info('小美', age=19)
user_info('小美', age=19, gender='女')


# 不定长参数
# (1).位置不定长 —— 参数为长度任意的元组
def user_tuple(*args):
    print(f"参数内容是{args}, 类型是{type(args)}")


user_tuple(1, 1.2, 'nc', True)


# (2).关键字不定长 —— 参数为长度任意的类字典,该特殊字典的关键字起名原则是变量起名，即数字、下划线、字母(自己给函数起形参名字，自己赋值)
def user_dict(**kwargs):  # key-word
    print(f"参数内容是{kwargs}, 类型是{type(kwargs)}")


user_dict(gender='女', age=16, a=4)


# 函数作为参数传递/函数调用
def test_func(hanshu):
    result = hanshu(2, 5)
    print(result)


def compute(xm, yn):
    return xm + yn


test_func(compute)


# 临时函数
# lambda 参数:函数体
test_func(lambda xm, yn: xm + yn)
