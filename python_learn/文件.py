"""
什么是编码？
编码是一种编码集合，记录了内容和二进制进行相互转换的逻辑。
最常用的编码是UTF_8。
为什么要使用编码？
计算机只认识0和1，需要将内容翻译为0和1才能保存计算机中。
同样也需要编码，将计算机保存的0和1，反向翻译回人可以识别的内容。
"""
# import time

"""
计算机关机后，内存中存放的数据会消失，故须使用硬盘、光盘、U盘等设备储存文件。
操作系统以文件为单位管理磁盘中的数据。
文件操作包括：打开、关闭、读写。
"""


# 该打开方式可以在执行操作后自动关闭文件不必手动关闭
# with open('D:/读取文件学习用.txt', 'r', encoding='UTF_8') as f:
#     index = 0
#     # for循环读取文件，默认按行赋值给控制变量
#     for line in f:
#         index += 1
#         print(f"第{index}行数据是：{line}")
#

# 打开文件
# open(name, mode, encoding)
# name:文件名，可以包含具体路径，没有具体路径则在当前代码同级路径下寻找或创建文件
# mode:'r'只读
#      ‘w’擦除写入
#      ‘a’追加写
#      所有模式都可以创建新文件
# encoding：编码格式，一般是UFT_8,该参数不是第三位，不能用位置参数，应用关键字参数直接指定
# f = open('D:/读取文件学习用.txt', 'r', encoding='UTF_8')
# f为该文件对象

# 读取文件
# read(num) 读取num个字符，num不指定则读取全部内容,非字节
# 多次使用读取函数会让光标向后移动
# print(type(f.read(4)))  类型是字符串
# print(f.read(4))

# readlines() 以行为单位读取全部内容并传入列表，列表的一个元素是一行文件内容
# print(f.readlines()[2])      # 类型是列表

# readline() 读取一行内容
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

# index = 0
# # for循环读取文件，默认按行赋值给控制变量
# for line in f:
#     index += 1
#     print(f"第{index}行数据是：{line}")
#
# time.sleep(10)  # 让程序继续持续运行10s
#
# # 关闭文件,否则占用系统资源
# f.close()

# 读取文件课后练习

# f1 = open('D:/读取文件学习用.txt', 'r', encoding='UTF_8')
#
# # 第一种方法
# # content = f1.read()
# # num = content.count('的')
# # print(num)
#
# # 第二种方法
# count = 0
# for line in f1:
#     line.strip('\n')  # 这一句不加的话，后面‘的’就要加‘\n’
#     # words = line.split(' ') 该句适合英文字母切割
#     for word in line:
#         if word == '的':
#             count += 1
#
# print(count)
#
# f1.close()

# w写出文件,再次打开文件，内容才会被清空
f2 = open('D:/写出文件学习用.txt', 'w', encoding='UTF_8')  # 若无该文件则创建新文件
f2.write('hello world')
# f2.flush()  # 将在内存中写入的内容更新到硬盘文件中
f2.write('dfghjkl')
# 'w'擦除写功能适用于再次打开文件并写入，同一次的文件打开过程是追加写
f2.close()  # 关闭函数自带更新功能

# a写出文件
f3 = open('D:/a写出文件学习用.txt', 'a', encoding='UTF_8')
f3.write('\n1、试验一下')
f3.write('\n2、我再试试')  # 已经是追加写了
f3.close()
