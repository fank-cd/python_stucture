#coding:utf-8
#栈
class Stack:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

#简单括号匹配
def parChecker1(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        #print len(symbolString)
       # print index
        #print symbol
        if symbol == '(':
            s.push(symbol)
            #print "="
        else:
            if s.isEmpty():
                balanced =False
                #print "null"
            else:
                s.pop()
                #print "pop"
        index = index +1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print parChecker1('((()))')
print parChecker1('(()')

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
                if not matches(top,symbol):
                    balaced = False
        index += 1
    if balaced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
        opens = "({["
        closers = ")}]"
        return opens.index(open) == closers.index(close)
print parChecker2('{{([][])}()}')
print parChecker2('[{()]')