# coding:utf-8
# 栈


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
# - O(1) 的复杂度实现一个 栈 的出栈入栈和返回 max、min 值的操作

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


# 简单括号匹配


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
# 符号匹配

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


# print parChecker2('{{([][])}()}')
# print parChecker2('[{()]')

# 除2 十进制转2进制

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


# print divideBy2(42)

# 十进制转8,16进制


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

# 中缀前缀和后缀表达式
# 中缀         前缀          后缀:
# A+B          +AB            AB+
# A+B*C       +A*BC          ABC*+
# (A+B)*C     *+ABC          AB+C*
