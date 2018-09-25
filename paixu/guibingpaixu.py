# coding:utf-8

def merge(left,right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result

def mergeSort(relist):
    if len(relist) <= 1:
        return relist
    mid_index = len(relist)/2
    left = mergeSort(relist[:mid_index])  # 递归拆解的过程
    right = mergeSort(relist[mid_index:])
    return merge(left,right)  # 合并的过程

print mergeSort([1,5,2,6,9,3])
