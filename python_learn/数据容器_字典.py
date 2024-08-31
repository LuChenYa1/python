"""
字典：键值对,自动去重
     无序，无下标索引，有key索引，同样用[]
     键和值均支持不同类型
{key1:value1, key2:value2, key3:value3, ...}
关键词：dict
符号：{}
含义：类似于学生——成绩，一个学生只能有一份成绩，但一份成绩可以有多位学生获得
当出现一位学生有多份成绩的情况，取最后的成绩作为真实成绩
key不允许重复、重复修改等于覆盖原有数据
可for循环，不支持while循环
应用场景：一批数据，可用key检索value的存储场景
"""

# 定义空字典
my_dict1 = {}
my_dict2 = dict()
my_dict3 = {'a': 100, 'f': 82, 'e': 69, 'c': 72, 202226001080: "陆沉涯"}
print(f"my_dict1的内容是{my_dict1}， 类型是{type(my_dict1)}")
print(f"my_dict2的内容是{my_dict2}， 类型是{type(my_dict2)}")
print(f"my_dict3的内容是{my_dict3}， 类型是{type(my_dict3)}")

score_f = my_dict3['f']
print(score_f)
name = my_dict3[202226001080]
print(name)

# 字典嵌套：
#       key不能为字典、列表、集合等可修改类型，是不可变量
#       value可以是任意数据容器的多次嵌套
student_dict = {"简":
                    {"语文": 78,
                     "数学": {89, 80},
                     "英语": 94
                     },
                "顾":
                    {"语文": [85, 87],
                     "数学": 84,
                     "英语": '97'},
                "黎":
                    {"语文": 75,
                     "数学": (90, 88),
                     "英语": 98}
                }
score_gu = student_dict["顾"]["数学"]
print(score_gu)

# 更新/增加元素
student_dict["简"]["语文"] = 81
student_dict["何"] = {
    "语文": 90,
    "数学": 96,
    "英语": 95}
print(student_dict)

# 删除元素
score = student_dict.pop("何")
print(student_dict)

# 获取全部key, 类型：<class 'dict_keys'>
keys = student_dict.keys()
print(f"内容是{keys},类型是{type(keys)}")

# 遍历字典
for key in keys:
    print(student_dict[key])

for Dict in student_dict:
    print(Dict, end=" ")
    print(student_dict[Dict])

# 计算元素数量
num = len(student_dict)
print(num)

# 清空元素
student_dict.clear()
print(student_dict)

# 练习
company_information = {'甲': {'部门': '科技部', '月薪': 3000, '级别': 1},
                       '乙': {'部门': '市场部', '月薪': 8000, '级别': 2},
                       '丙': {'部门': '科技部', '月薪': 4000, '级别': 1},
                       '丁': {'部门': '市场部', '月薪': 4500, '级别': 1}}
for key in company_information:
    if company_information[key]['级别'] == 1:
        company_information[key]['级别'] += 1
        company_information[key]['月薪'] += 1000
    print(key, company_information[key])

