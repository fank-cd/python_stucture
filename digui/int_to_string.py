#coding:utf-8

def toStr(n,base):
    """

    :param n: 要转换的整数
    :param base: 要转换的进制
    :return: 返回一个
    """
    convertString = "0123456789ABCDEF"

    if  n < base:
        return convertString[n]
    else:
        return toStr(n/base,base) + convertString[ n%base]

print toStr(10,2)