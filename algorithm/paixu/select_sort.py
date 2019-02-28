#coding:utf-8

# O(n^2)
# 选择排序是不断去查找列表中最小值，第一次找最小值，交换位置，第二次找次小值，交换位置。
# 这里使用了新的列表，实际可能不需要新的空间


def findSmall(arr):
    smallest = arr[0]  # 存储最小值，默认为列表第一位
    smallest_index = 0  # 存储最小值的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmall(arr)
        newArr.append(arr.pop(smallest))  # 找出列表中最小值，并加入新数组中然后从原数组中删去

    return newArr


l = [5, 7, 2, 1, 3]
# print selectionSort(l)


def select_sort(li):
    for i in range(len(li) -1):
        min_index = i  # 最小值的索引假设为i

        for j in range(i+1, len(li)):  # i+1这里表示0-i的数是默认有序的，已经找到了的。所以需要遍历的为i+1-len
            if li[j] < li[min_index]:
                min_index = j  # 循环到找到剩下的最小值的索引

        if min_index != i:  # min_index 如果发生了交换，则最小值不是默认的i和li[i]，两者交换
            li[i], li[min_index] = li[min_index], li[i]

    return li


print select_sort(l)