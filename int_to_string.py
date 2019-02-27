#coding:utf-8
from structure.stack import Stack

rStack = Stack()


def toStr(n,base):
    """

    :param n: 要转换的整数
    :param base: 要转换的进制
    :return: 返回一个
    """

    convertString = "0123456789ABCDEF"

    while n > 0:

        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


print(toStr(1453, 16))
print(toStr(10, 2))
