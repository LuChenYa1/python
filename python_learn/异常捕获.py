"""
代码中往往容易出现各种BUG
一旦出现
整个程序运行崩溃
所以需要补救措施

try: 原来要执行的代码，可能会发生异常
！！！！！！！注意，try中如果出现异常，并不是全部语句不执行，只是报错语句不执行，其他会执行，报错语句前后的正常语句都会正常执行
except:如果出现错误，又满足except的报错要求，则执行该代码，一般为补救措施
else:未出现异常，则执行该句
finally：不管出不出现异常，该句都要执行

异常具有传递性
即调用了该异常的函数或语句都会异常
导致一连串报错
"""

# try:
#     f = open('实验.txt', 'r', encoding='UTF_8')
#     f.close()
#     # FileNotFoundError
# except:  # 尽可能不用空的，没有任何特定异常的except，会报警告
#     print('出现异常')

# 多except捕获不同异常，给出不同解决方案
try:
    1 / 0
except NameError as e:  # 这里的e承载了报错信息
    print(e)
    # NameError:变量未定义
except ZeroDivisionError as Z:  # 被0除错误
    print(Z)

# 多异常写在一个except中，用元组装
try:
    1/0
    print(numpy)  # 这里说明，出现多个异常，优先看第一个异常
except (NameError, ZeroDivisionError) as e:
    print("报错啦！！！")
    print(e)

# 一次性检测所有异常，但不要用空except
try:
    print(name)
    1/0
except Exception as e:
    print('出现异常，请修改')
    print(e)
    print()

# 最后两个，可加可不加,可以增加代码的完整性
# 示范
try:
    print("看一下没有异常的语句会不会执行，好吧会执行")
    f1 = open('D:/123.txt', 'r', encoding="UTF_8")
    print("再试一下")
except Exception as e:
    print(e)
    print('出现异常')
    f1 = open('D:/123.txt', 'w', encoding="UTF_8")  # 补救措施
else:
    print('如果没有出现异常，那else就要执行，也就是说，try和else同生死共进退')
finally:
    print('不管有没有异常，都要执行finally')
    f1.close()

def func1():
    print("C1调用开始")
    4/0
    print("C1调用结束")

def func2():
    print("C2调用开始")
    func1()
    print("C2调用结束")

def main():
    func2()

# if __name__ == '__main__':
#     main()

try:
    main()
except Exception as e:
    print(e)
