# coding:utf-8

# O(n^2)

# i 范围 0- (len-1)
# j 范围 0- (i-1) j永远比i小1
def insertSort(relist):
    len_ = len(relist)
    for i in range(1,len_):
        for j in range(i):
            if relist[i] < relist[j]:
                relist.insert(j,relist[i])  # 首先碰到第一个比自己大的数字，赶紧刹车，停在那，所以选择insert
                relist.pop(i+1)  # 因为前面的insert操作，所以后面位数+1，这个位置的数已经insert到前面去了，所以pop弹出
                break
    return relist

print insertSort([1,5,2,6,9,3])
# 插入排序在最好情况下，需要比较n-1次，无需交换元素，时间复杂度为O(n);在最坏情况下，时间复杂度依然为O(n2)