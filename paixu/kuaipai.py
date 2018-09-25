# coding:utf-8

# 取第一个数为基准数
# 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
# 再对左右区间重复第二步，直到各区间只有一个数。


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [j for j in array[1:] if j > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


print quickSort([1, 5, 2, 6, 9, 3])
