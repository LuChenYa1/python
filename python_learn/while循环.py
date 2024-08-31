"""
实现从1连加到100
"""
i = 0
s = 0
while i < 101:
    s += i
    i += 1
print("从1加到100的值是%d" % s)

"""
实现99乘法表
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}", end="\t ")
        j += 1
    print(" ")
    i += 1
