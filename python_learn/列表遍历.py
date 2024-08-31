"""
for循环和while循环
都能用于遍历列表

"""

# while循环遍历字符串列表
def bianli():
    my_list = ["twitter", "xiao"," "]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(element)
        index += 1

# for循环遍历列表，该列表不需要全是数字，是字符串也行
def prebianli():
    pre_list = ["xiao", "lanniao", 2, 1.35]
    for index in pre_list:
        print(index)

# for循环遍历数字列表
def bianlishuzi ():
    shuzi_list = [1, 2, 3, 4, 5]
    for index in shuzi_list:
        print(index)


# bianli()
prebianli()
# bianlishuzi()


# 练习案例：遍历并取出偶数,并放到新列表里
index = 0
lianxi_list = [1, 3, 6, 5, 8]
list_oushu = []
while index <len(lianxi_list):
    if lianxi_list[index] % 2 == 0:
        print(f"偶数是{lianxi_list[index]}")
        list_oushu.append(lianxi_list[index])
    index += 1
for x in list_oushu:
    print(x)