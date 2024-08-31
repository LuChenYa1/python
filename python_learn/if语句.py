"""
多条件执行语句只执行其中一条
在多个条件满足的情况下，
仍旧只执行从上到下遇到的第一个满足条件的语句
"""
import random
# print("欢迎来到黑马游乐园，儿童免费，成人收费")
# age = int(input("请输入您的年龄："))
# height = float(input("请输入您的身高："))
# vip_level = int(input("请输入您的vip级别（1~5）："))
# if age >= 18:
#     print("您已成年，需补票10元")
# elif height <= 140 & age < 18:
#     print("您未成年，可享受免票待遇")
# elif vip_level >= 3:
#     if age == 1:
#         print("这是嵌套if")
#     else:
#         print("利用缩进划分层级")
#     print("前面都不符合条件，才会执行该语句")
# else:
#     print("您未成年，但身高不符合要求，需补票5元")
# print("祝您游玩愉快")

# 简单猜数字游戏
count = 0
guess_num = 0
target_num = random.randint(1, 100)
while True:
    count += 1
    guess_num = int(input("请输入你猜想的数字："))
    if guess_num == target_num:
        print("恭喜第%d次就猜对了呢" % count)
        break
    else:
        if guess_num >= target_num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")
