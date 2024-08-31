"""
python中的for循环无法控制循环次数和顺序
for 临时变量 in 待处理数据集
将数据集中的数据依次赋值给临时变量
该数据集可以是字符串之类的
直到数据集遍历完毕，退出循环
range()表示获得一个数字序列
常用于for循环
"""
import random
# range(num2)
# 默认从0到num2-1，不包含num2本身
# range(num1,num2)
# 从num1到num2，不包含num2本身
# range(num1,num2,step)
# 从num1到num2，不包含num2本身,且间隔为step
for x in range(9):
    print(x)
for x in range(2, 9):
    print(x)
for x in range(2, 9, 3):
    print(x)

#  统计字符串中有几个字母i老师
count1 = 0
name = "heima_it is a teacher"
for x in name:
    if x == 'i':
        count1 += 1
print(f"总共有{count1}个‘i’")

# 统计从1到100有几个偶数
count2 = 0
for x in range(1, 100):
    if x % 2 == 0:
        count2 += 1
print("总共有%d个偶数" % count2)

# for循环内部的变量在其外部可以访问，但不规范
i = 1
for x in range(3):
    i = 4
print(i)

# 九九乘法表
i = 0
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={i*j}", end="\t")
    print("")
# break结束所在循环
# continue结束当次循环，开启下次循环

# 训练案例：发工资
salary = 10000
for name in range(1, 21):
    jixiao = random.randint(1, 10)
    if jixiao < 5:
        print(f"员工{name},绩效{jixiao},低于5，不发工资，下一位。")
        continue
    if salary == 0:
        if name !=20:
            print("工资发完了，下个月再来吧")
        break
    salary -= 1000
    print(f"向员工{name}发放工资1000元，账户余额还剩{salary}元。")

