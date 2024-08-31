def str_reverse(s):
    """
    接收传入的字符串，倒序返回
    :param s:将被反转的字符串
    :return:反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    按照下标x和y，对字符串切片
    :param s:将被切片的字符串
    :param x:切片的开始下标
    :param y:切片的结束下标
    :return:切片完成以后返回的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    # 测试完成
    con1 = str_reverse('黑马程序猿')
    con2 = substr('黑马程序猿', 2, 4)
    print(con1)
    print(con2)
