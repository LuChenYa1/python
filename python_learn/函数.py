"""
函数没有返回值时，其结果的类型是None
None类似于0和布尔类型False
None是空集，0是含元素0的集合
"""
print(type(None))
# <class 'NoneType'>
# 需要用到但暂时不需要赋值的变量可以赋值None
x = None
# 但好像没有0方便，会有类型错误，一般还是用0赋值


def fun(t):
    print("欢迎光临，请出示健康码，并配合检测温度")
    if t > 37.5:
        print(f"您的体温是{t},需要隔离")
    else:
        print(f"您的体温是{t},正常请进")


fun(37)
fun(38)


def check_age(age):
    if age >= 18:
        return True
    # 1 == True
    else:
        return None
    # 0 == False == None


result = check_age(1)
if not result:
    # result为假时进入
    print("你是未成年哦")
else:
    print("您已成年")


def multiply(m, n):
    """
    两数相加(函数说明文档)
    :param m:数x
    :param n: 数y
    :return: 结果
    """
    result1 = m + n
    m += 1
    return result1


# 非地址传参无法改变原值，和C语言一样
i = 1
j = 2
sum1 = multiply(i, j)
print(sum1)
print(i)

# 变量在函数中的作用域
# 发现在python中，由于定义变量无需写类型，导致声明变量和定义变量区分不开
# 写上变量名和‘=’就算声明
num = 200
num = 300
num += 300


def fun_a():
    num = 500
    num = 300
# 函数内定义的一般是局部变量，作用域仅在函数内部


def fun_b():
    global num
    num = 600
# 加关键字global可以将局部变量声明为全局变量
# 从而在函数内部改变全局变量的值
fun_a()
fun_b()
print(num)


name = None
money = 5000000


def query(show_header):
    global money
    global name
    if show_header:
        print("----------查询余额----------")
    print(f"您好，{name},您当前的余额是{money}元")

def saveing():
    global money
    global name
    print("----------存款----------")
    money += int(input("您要存多少钱："))
    query(False)

def get_money():
    global money
    global name
    print("----------取款----------")
    money -= int(input("您要取多少钱："))
    if money <= 0:
        print("您的余额不足，无法取出")
    else:
        query(False)


def menu():
    print("---------主菜单--------")
    print("查询余额\t[输入1]")
    print("存款   \t[输入2]")
    print("取款   \t[输入3]")
    print("退出   \t[输入4]")
    return input("请输入您的选择：")


name = input("欢迎使用ATM，请输入您的姓名:")
print(f"您好，{name}")
while True:
    order = menu()
    if   order == "1":
        query(True)
    elif order == "2":
        saveing()
    elif order == "3" :
        get_money()
    elif order == "4":
        break
    else:
        print("输入错误，退出程序")
        break

