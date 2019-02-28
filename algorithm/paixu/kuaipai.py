# coding:utf-8

# 取第一个数为基准数
# 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
# 再对左右区间重复第二步，直到各区间只有一个数。


# def quickSort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i < pivot]
#         greater = [j for j in array[1:] if j > pivot]
#         return quickSort(less) + [pivot] + quickSort(greater)
#
#
# print quickSort([1, 5, 2, 6, 9, 3])


def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


l = [1, 5, 2, 6, 9, 3]
quick_sort(l, 0, len(l)-1)

print l

