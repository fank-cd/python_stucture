# coding:utf-8

# 每次排序找到最大值 放到末尾
# O(n^2)

def selectionSort(alist):

    for fillslot in range(len(alist)-1, 0, -1):  # range(x,0,-1) 翻转
        positionOfMax=0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location  # 记录最大值的序号

        alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)
