"""
集合：
无序、不允许重复、可修改，不支持下标索引
关键字：set
可for循环，不支持while循环
应用场景：一批数据，去重存储场景
"""

my_set = {"C语言", "Python", "java", "Python", "C#", 4}
# 注意这里的空集合只能用set(),不能用{}定义
my_set_empty = set()
print(f"my_set的内容是{my_set}，类型是{type(my_set)}")  # 每次打印出来的都不一样，因为集合是无序的
print(my_set_empty)

# add
my_set.add("C++")
my_set.add("Python")
# 集合本身被修改
print(my_set)

# remove
my_set.remove("Python")
print(my_set)

# pop随机移除并返回该元素
element = my_set.pop()  # 一般默认取打印顺序的第一个
print(element, my_set)

# 清空集合
my_set.clear()

# 在集合1内，寻找与集合2不同的元素
set1 = {1, 5, 9, 6, 0}
set2 = {1, 3, 2, 8}
set3 = set1.difference(set2)
print(set3)

# 在集合1内，删除与集合2相同的元素，无返回值
set1.difference_update(set2)
print(f"set1是{set1}")

# 两个集合合并
set5 = set1.union(set2)
print(set5)

# 统计集合元素数量，自动去重
set6 = {1, 2, 3, 4, 5, 2, 4, 1, 5, 3}
num = len(set6)
print(f"集合包含的元素数量是{num}")

# for循环遍历集合，由于集合不支持下标索引，故无法用while循环遍历
count = 1
for element in set6:
    print(f"set6的第{count}个元素是{element}")
    count += 1

# 课后练习
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', "best"]
set_target = set()
for element in my_list:
    set_target.add(element)
# set_target.add(my_list)
print(my_list)
print(f"去重后的集合为{set_target}")
