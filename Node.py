#coding:utf-8
#无序列表：链表

class Node:
    def __init__(self,inindata):
        self.data = inindata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

#temp =Node(93)
#print temp.getData()

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current= current.getNext()
        #print current.getData()
        return found

    def remove(self,item):
        current =self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)

print mylist.head.getNext().getData()
mylist.head = mylist.head.getNext()
print mylist.head.getNext().getData()
mylist.head = mylist.head.getNext()
print mylist.head.getNext()
#print mylist.search(17)