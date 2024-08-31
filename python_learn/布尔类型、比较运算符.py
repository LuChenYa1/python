"""
布尔类型属于数据的一种类型，只有True和False两个字面量
"""

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1的内容是 {bool_1}", type(bool_1))
print(f"bool_2的内容是 {bool_2}", type(bool_2))

# 比较运算符的运用
# == != <= >= < >
num1 = 10
num2 = 20
num3 = 10
print(f"10==20的结果是 {num1==num2}")
print(f"10>=20的结果是 {num1>=num2}")
print(f"10<=20的结果是 {num1<=num2}")
print(f"10==10的结果是 {num1==num3}")

str1 = "hello"
str2 = "world"
print(f"hello!=world的结果是 {str1!=str2}")
print(f"hello==world的结果是 {str1==str2}")

