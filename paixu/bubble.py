# coding:utf-8

# O(n^2)


def bubble_sort(li):

    if len(li) >= 2:
        for j in range(len(li) - 1):
            for i in range(1, len(li)):
                if li[i] > li[i - 1]:
                    li[i], li[i - 1] = li[i - 1], li[i]
    else:
        li = li[::-1]
    return li



# print bubbleSort(alist)
# print bubble_sort(alist)


# 短冒泡(加了一个标志位)
def bubble_sort_opt(li):
    if len(li) >= 2:
        for j in range(len(li)-1):
            flag = False
            for i in range(1, len(li)):
                if li[i] > li[i-1]:
                    li[i], li[i-1] = li[i-1], li[i]
                    flag = True

            if not flag:
                break
    else:
        li = li[::-1]
    return li


