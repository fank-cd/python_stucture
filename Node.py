# coding:utf-8


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListOneway(object):
    def __init__(self, node=None):
        self.__head = node

    def __len__(self):
        cur = self.__head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        return count

    def is_empty(self):
        return self.__head == None

    def add(self, value):
        # 插在头部
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def append(self, value):
        # 插在尾部
        node = Node(value)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, value):

        if pos <= 0:  # 插入位置小于0，则直接插在头部
            self.add(value)
        elif pos > len(self) - 1:  # 插入位置大于长度，则直接插在尾部
            self.append(value)
        else:
            node = Node(value)
            prior = self.__head
            count = 0

            while count < (pos-1):
                prior = prior.next
                count += 1

            node.next = prior.next
            prior.next = node

    def remove(self, value):
        cur = self.__head
        prior = None
        while cur:
            if value == cur.value:
                if cur == self.__head:
                    self.__head = cur.next

                else:
                    prior.next = cur.next
                break
            else:
                prior = cur
                cur = cur.next

    def search(self, value):
        cur = self.__head
        while cur:
            if value == cur.value:
                return True
            cur = cur.next

        return False

    def traverse(self):
        cur = self.__head
        while cur:
            print cur.value
            cur = cur.next


l = LinkedListOneway()

l.add(2)
l.add(4)
l.append(3)
# print l.search(2)
l.insert(0, 5)
l.insert(4, 5)

l.remove(2)
l.traverse()
