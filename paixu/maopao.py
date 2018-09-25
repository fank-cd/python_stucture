# coding:utf-8

# O(n^2)


def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            # print(passnum, i)
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                """ 
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                """


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

# 短冒泡


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum-1


alist=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)


def bubbleSort(relist):

    len_ = len(relist)
    print(len_)
    for i in range(len_):
        for j in range(0, len_-i-1):
            print(i, j)
            if relist[j] > relist[j+1]:
                relist[j+1], relist[j] = relist[j], relist[j+1]
    return relist

print bubbleSort([1,5,2,6,9,3])

