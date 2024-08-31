"""
序列：
内容连续、有序、可使用下标索引的一类数据容器
列表、元组、字符串都是序列
序列[起始下标：结束小标：步长]
取数据操作不影响序列本身
"""

# 对list进行切片
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:5:2]
print(result1)

# 对tuple进行切片,不写默认取全部元素
my_tuple = ('h', 2, 3, 9.0)
result2 = my_tuple[::]
print(result2)

# 对str进行切片
my_str = "itheima and itcast"
result3 = my_str[::3]
print(result3)
result4 = my_str[6:1:-1]  # 倒着、按步长取数据ffffff
print(result4)

# 应用:取出8765
str1 = "01234, 56789, 02538"
s1 = str1.split(",")[1].replace("9", "")[::-1]
print(f"第一种方法：{s1}")
s2 = str1[6:11][::-1]
print(f"第二种方法：{s2}")
