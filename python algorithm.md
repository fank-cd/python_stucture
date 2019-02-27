递归
---
就是自己调用自己的一种方法，二叉树中的前中后遍历非常典型

- 汉诺塔游戏
- fib
```
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

```

查找算法
---

- 顺序查找

就是一直for循环，很基础的东西。

**时间复杂度 O(n)**
```
def linear_search(list,value):
    for i in list:
        if i == value:
            return True
        else:
            return False
```

- 二分查找 

要求必须有序列表。思想为一半一半的去查找，看目标值在偏小还是偏大，然后替换左或者右端点。

**时间复杂度O(logn)**

非递归版本：
```

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

    
```

递归版本：
```
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

```

排序算法
---

- 冒泡
两两相比，交换顺序

**时间复杂度O(n\*2)**

代码：
```
def bubble_sort(li):

    if len(li) >= 2:
        for j in range(len(li) - 1):
            for i in range(1, len(li)):
                if li[i] > li[i - 1]:
                    li[i], li[i - 1] = li[i - 1], li[i]
    else:
        li = li[::-1]
    return li

```

- 短冒泡

加入了一个标志位，如果某一次的循环中，没有进行交换，则此时已经为排序状态，则break退出
```
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


```
