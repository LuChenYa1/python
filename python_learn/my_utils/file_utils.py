def print_file_info(file_name):
    """
    1、接收传入文件的路径/名字，打印文件内容
    2、如果文件不存在就捕获异常，输出提示信息
    3、文件存在就finally关闭文件
    :param file_name:文件名字
    :return:无
    """
    f = None  # 预先给值，用于判断文件是否存在
    try:
        f = open(file_name, 'r', encoding='UTF_8')
        print(f.read())
    except Exception as e:
        print(f'文件出现异常，原因是{e}')
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
     将data写入接收的文件中
     :param filename: 文件名字
     :param data: 要写入的数据
     :return: 无
    """
    f = open(file_name, 'a', encoding='UTF_8')
    f.write('\n')
    f.write(data)
    f.close()


if __name__ == '__main__':
    append_to_file('D:/123.txt', '是的风格和健康')
    print_file_info('D:/123.txt')