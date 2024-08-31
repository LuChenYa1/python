"""
json是一种通用的数据格式
常用于不同编程语言之间的数据传递
其本质是字符串
字符串内容是字典或装着字典的列表
在python中使用json数据格式具有优势
要用到的模块是json
json字符串最外面必须是单引号
"""

import json

# 将列表转换为JSON
data1 = [{'name': '张大山', 'age': 19}, {'name': '李小虎', 'age': 20}, {'name': '刘大锤', 'age': 18}]
json_str = json.dumps(data1, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将字典转换为JSON
data2 = {'name': '张大山', 'age': 19}
json_str = json.dumps(data2, ensure_ascii=False)  # 缺省参数，用于防止中文转换乱码
print(type(json_str))
print(json_str)

# 将JSON字符串转换为python列表
# 避坑！！！！这里json字符串外面必须是单引号，为防止和内部字典的key撞上，key要用双引号
s = '[{"name": "张大山", "age": 19}, {"name": "李小虎", "age": 20}, {"name": "刘大锤","age": 18}]'
py_list = json.loads(s)
print(type(py_list))
print(py_list)

# 将JSON字符串转换为python字典
s = '{"name": "陈小二", "age": 21}'
py_dict = json.loads(s)
print(type(py_dict))
print(py_dict)
