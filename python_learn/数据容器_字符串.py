"""
字符串是一种不可修改的数据容器、有序、可下标索引，可以重复
这点类似元组
字符串既可以用”“，也可以用‘’
反斜杠\\ 加 ” 或者 ‘ 输出 " 或’
应用场景：一串字符串的存储场景
"""
# 在字符串内包含双引号
name = '"黑马程序员"'
print(name)

# 在字符串内包含单引号
name = "'黑马程序员'"
print(name)

# 使用转义字符，解除引号效用
name = "\"黑马程序员\'"
print(name)
# W292 no newline at end of file:文件末尾要加换行符

"""
字符串拼接+
多用于字符串与字符串的拼接，字符串和数字不能用+拼接：应为类型 'str'，但实际为 'int' 
和逗号的区别是为了省略空格
"""
name = 50
print("我有", name, "元,花了10元")
string = "我还剩"
print(string + "多少钱")

"""
字符串格式化：
%s，%d,%f 占位符，可拼接数字变量
将数据放入要占位的地方
一个%只能接收一个数据
多个数据要加括号
m.n:m控制宽度，超出无效，n控制小数位数，偶数位四舍五入
"""

# 拼接字符串
num1 = "黑马程序员"
num2 = "我学python用%s" % num1
print(num2)

# 拼接数字
age = 18
height = 158.5485
sen1 = "我今年%s岁，身高%scm" % (age, height)
print(sen1)
name_s = "陆沉涯"
sen2 = f"我的名字是{name_s}，今年{age}岁，高{height}"
print(sen2)
print("我的名字是%s，今年%d岁，高%.1f" % (name_s, age, height))

# 一种拼接更加快捷的方式:f {数据名} ，不作精度控制，也没有类型限制
print(f"我的名字是{name_s}，今年{age}岁，高{height}")

"""
表达式格式化
确保类型对应的值是一样就行
"""
print("字符串在python中的类型是%s" % type("str"))
print(f"2*4={2 * 4}")
print("2*4=%d" % 2 * 4)  # 不加括号会重复4遍
print("2*4=%d" % (2 * 4))

# 字符串支持正向和反向索引
str1 = "haima cheng xu yuan"
print(str1[15])
print(str1[-4])

# 查找元素或多个元素下标,返回首元素的下标
num_num = str1.index("che")
print(f"'che'的下标是{num_num}")

# 字符串替换
# 需要注意的是，字符串本身不能修改，所以是对拷贝出来的内容进行修改，并放入新字符串中
old_str = "itheima and itcast"
new_str = old_str.replace("it", "程序")
print(old_str)
print(new_str)

# 将字符串内容按照某个元素进行切割，并存入列表中，字符串本身不变
str_list = old_str.split(" ")  # 按照空格分割,这里要注意，选定划分元素如果是空格，也需要在双引号之间留空，和字符串默认结尾的\0无关
print(f"old_str经切割后形成的新列表是{str_list}, 类型是{type(str_list)}")

# 去除开头和结尾的指定字符串或字符:
# 将strip()内部的要去除的字符串分为多个目标字串
# 在源字符串的开头从前往后和结尾从后往前查找这些目标字串
# 一旦找到就删除它们
# 但一旦出现非目标字串就停止查找
# 即使中间可能还有目标字串
aim_str = "      12ithei211mtia and i2tcast2121112    "
new_str1 = aim_str.strip("1 2")  # 去除前后空格
print(f"{aim_str}被strip()后变成了{new_str1}")

# count记录目标字串出现次数
num_it = aim_str.count("it")
print(f"'it'在{aim_str}中出现的次数是{num_it}")

# len记录长度
num_len = len(aim_str)
print(f"'aim_str'的长度是{num_len}")

# 字符串遍历
for x in old_str:
    print(x, end="")
print()

index = 0
while index < len(old_str):
    print(old_str[index], end="")
    index += 1
