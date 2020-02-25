import time


def time_to_string(timestap):
    """将时间戳转换字符串时间"""
    to_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestap))
    return to_string
