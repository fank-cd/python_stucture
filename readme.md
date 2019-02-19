##  数据结构


 栈
---
- push()     把一个元素添加到栈的最顶层
- pop()      删除栈最顶层的元素，并返回这个元素
- peek()     返回最顶层的元素，并不删除它
- isEmpty()  判断栈是否为空
- size()     返回栈中元素的个数


#### 代码如下

```
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

```


#### 变种

- O(1) 的复杂度实现一个 栈 的出栈入栈和返回 max、min 值的操作
> 设置一个辅助栈来存入当前最小值，如果push的item小于等于辅助栈顶元素，则都入栈，否则不入辅助栈。出栈时如果和辅助栈元素相等则都出栈，max操作同理。
```
class Stack(object):
    def __init__(self):
        self.items = []
        self.min_items = []
        self.max_items = []

    def push(self,item):
        self.items.append(item)

        if self.min_items == [] or item <= self.min_items[::-1]:
            self.min_items.append(item)

    def pop(self):
        if self.min_items[::-1] == self.items[::-1]:
            self.items.pop()
            self.min_items.pop()
        else:
            self.items.pop()


    def peek_min(self):
        print self.min_items[::-1]
        return self.min_items[::-1]


```

- 简单括号匹配


```
def parChecker1(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        # print len(symbolString)
        # print index
        # print symbol
        if symbol == '(':
            s.push(symbol)
            # print "="
        else:
            if s.isEmpty():
                balanced = False
                # print "null"
            else:
                s.pop()
                # print "pop"
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
# print parChecker1('((()))')
# print parChecker1('(()')
```


- 符号匹配("({[")


```
def parChecker2(symbolString):
    s = Stack()
    balaced = True
    index = 0

    while index < len(symbolString) and balaced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balaced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balaced = False
        index += 1
    if balaced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)

```

- 进制转换

除2 十进制转2进制


```
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        # print rem
        remstack.push(rem)
        decNumber = decNumber / 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
        # print binString
    return binString
```


十进制转8,16进制



```
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        # print rem
        remstack.push(rem)
        decNumber = decNumber / base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    return newString
# print baseConverter(25,2)
# print baseConverter(233,16)
# print baseConverter(25,16)
```
