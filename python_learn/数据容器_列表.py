"""
数据容器：一种可以容纳多个数据的数据类型，每一个元素都可以是任意类型，如字符串、数字，布尔类型
包括列表、元组、字符串、集合、字典
应用场景：一批数据，可修改、可重复的存储场景
"""


# 列表：容量是2^63-1,有序存储，可以嵌套，可修改，可以是不同类型，包含一些初始内置函数，用于增删改除
# 下标从左到右从0开始+1，从右到左从-1开始-1
mylist = [1, "我是你爹", True, 1]
mylist_1 = [1, 2, 3, 6, 4]
mylist_2 = [[2, 'yi', 3.12], ['5555'], [False, 0]]
print(mylist)
print(mylist_1)
print(mylist_2)
print(mylist[1])  # "我是你爹"
print(mylist_1[-2])  # 6
print(mylist_1[-3])  # 3
print(mylist_1[-4])  # 2
print(mylist_2[2][0])
print(type(mylist))

# list列表的常用操作

alist = ["黑泽尔", "加兰", "滕瑞雨", "钱错"]
# 1.查找某元素在列表内的下标,被查找的元素如果不存在，会报错
a = alist.index("加兰")
print(a)
# 2.修改特定位置的值
alist[2] = "瑞瑞"
print(alist)
# 3.在指定位置插入新元素
alist.insert(2, "都是He结局")
print(alist)
# 4.在列表尾部追加新元素
alist.append("他们与共到白头")
print(alist)
# 5.在列表尾部追加一组数据
blist = ["夙又", "赵暮涯"]
alist.extend(blist)
print(alist)
# 6.1删除指定位置元素
del alist[2]
print(alist)
# 6.2删除指定位置元素并返回该元素
element = alist.pop(4)
print(alist, element)
# 7.移除特定内容元素，只移除匹配到的第一个元素
alist.remove("钱错")
print(alist)
# 8.清空列表
alist.clear()
print(alist)
# 9.统计某元素的数量
clist = ["一", "二", "一", "三", "三"]
num = clist.count("一")
print(num)
# 10.统计该列表的全部元素数量
Sum = len(clist)
print(Sum)
