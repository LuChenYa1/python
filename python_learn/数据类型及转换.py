"""
type()用于查看字面量的数据类型
变量没有类型
返回值是描述类型的字符串
"""

# 1使用print直接输出数据类型
print(type(13.14))
print(type(666))
print(type("黑马程序员"))
print(" ")  # 空格一行

# 2使用变量存储type()语句的结果
float_type = type(13.14)
int_type = type(666)
string_type = type("黑马程序员")
print(float_type)
print(int_type)
print(string_type)
print(" ")

# 3使用type()，查看变量中存储的数据的类型信息
num_float = 13.14
num_int = 666
num_string = "黑马程序员"
f_type = type(num_float)
i_type = type(num_int)
s_type = type(num_string)
print(f_type)
print(i_type)
print(s_type)

"""
强制类型转换
与c语言不同，括号括的是数据
数字都可以转换为字符串
但字符串只有内容为数字的可以转换为数字
"""
# 将数字转换为字符串
num_str1 = str(666)
print(type(num_str1), num_str1)
num_str2 = str(11.135)
print(type(num_str2), num_str2)
print(" ")

# 将字符串转换为数字
num_float = float("13.14")
print(type(num_float), num_float)
num_int = int("12345")
print(type(num_int), num_int)

"""
错误示范：
num_int = int("heima")
print(type(num_int), num_int)

ValueError: invalid literal for int() with base 10: 'heima'
"""
# 将浮点数转换为整形
float1 = int(123.65)
int1 = float(455678)
print(f"float1的值是{float1}，int1的值是{int1}")
# 直接取整，不符合四舍五入

