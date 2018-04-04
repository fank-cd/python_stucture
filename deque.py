#coding:utf-8
#deque ：双端队列
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append((item))

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

#回文检查

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        #print '1'
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last :
            stillEqual = False
    return stillEqual

print palchecker('asdsa')
print palchecker("radar")
print palchecker("lalksjfklasdjf")
#s = "a,b. d"
s ='abcba'
l =list(s)
print l
print l.reverse()
print l