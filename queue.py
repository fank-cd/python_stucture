# coding:utf-8
# 队列（单向）


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def item(self):
        return self.items


"""
q = Queue()
q.enqueue(4)
q.enqueue(6)
q.enqueue(1)
print q.size()
print q.dequeue()
print q.size()
"""

# 烫手山芋


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
        #print simqueue.item()
    while simqueue.size() > 1:
        #print simqueue.item()
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            #print simqueue.item()
        simqueue.dequeue()
    return simqueue.dequeue()


namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
#print hotPotato(namelist,7)
