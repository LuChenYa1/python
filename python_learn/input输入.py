"""
提示语句可直接写在输入语句内
从键盘上输入的任何数据都是字符串
"""
name = input("Please tell me your name:")
age = input("Please tell me your age:")
height = input("Please tell me your height:")
print(f"I know,you are {name},your age is {age},and you are {height} cm high")
print(type(age))
