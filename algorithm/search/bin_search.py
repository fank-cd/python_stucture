# coding:utf-8

# 二分要求列表有序，返回的是元素的索引
# 二分查找是不断查找中间位置的值和要查找的值做比较，不断调整猜测地范围来调整中间值
# 复杂度 O(logn)


# 递归版本
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]

# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))


# 非递归版本

def binary_search(li, item):
    low = 0
    high = len(li) - 1
    # low和high表明查找范围

    while low <= high:
        # 只要范围没有缩小到只包含一个元素
        mid = (low+high)/2  # 中间位置
        guess = li[mid]  # 猜测的元素
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print binary_search(testlist, 8)
