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


#### 拓展

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


链表
---

一个节点类，一个列表类组成

- is_empty() 链表是否为空
- length() 链表长度
- travel() 遍历整个链表
- add(item) 链表头部添加元素
- append(item) 链表尾部添加元素
- insert(pos, item) 指定位置添加元素
- remove(item) 删除节点
- search(item) 查找节点是否存在 

```

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

    def remove(self,value):
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
#print l.search(2)
l.insert(0,5)
l.insert(4,5)

l.remove(2)
l.traverse()

```

#### 拓展

- 快慢指针 

其实就是两个指针，一个快指针，一个慢指针。

可以应用的题目是寻找链表中间元素、循环链表、求倒数第 N 个节点

假如我们设置 两个指针 slow、fast 起始都指向单链表的头节点。其中 fast 的移动速度是 slow 的2倍。当 fast 指向末尾节点的时候，slow 正好就在中间了。想想一下是不是这样假设一个链表长度为 6 ， slow 每次一个节点位置， fast 每次移动两个节点位置，那么当fast = 5的时候 slow = 2 正好移动到 2 的节点的位置



单向队列
---
先解释一下，python自己是有队列的，这里主要是用python去实现队列这种数据结构，便于理解和应用。

##### 先进先出 FIFO

- Queue() 创建一个空的新队列。 它不需要参数，并返回一个空队列。
- enqueue(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
- dequeue() 从队首移除项。它不需要参数并返回 item。 队列被修改。
- isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
- size() 返回队列中的项数。它不需要参数，并返回一个整数。



#### 代码

```
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


```

#### 拓展

- 烫手山芋问题

这个游戏相当于著名的约瑟夫问题，一个一世纪著名历史学家弗拉维奥·约瑟夫斯的传奇故事。故事讲的是，他和他的 39 个战友被罗马军队包围在洞中。他们决定宁愿死，也不成为罗马人的奴隶。他们围成一个圈，其中一人被指定为第一个人，顺时针报数到第七人，就将他杀死。约瑟夫斯是一个成功的数学家，他立即想出了应该坐到哪才能成为最后一人。最后，他加入了罗马的一方，而不是杀了自己。你可以找到这个故事的不同版本，有些说是每次报数 3 个人，有人说允许最后一个人逃跑。无论如何，思想是一样的。


####代码

```
def hotPotato(namelist, num):
    simqueue = Queue()
    
    for name in namelist:  # 将所有人入列
        simqueue.enqueue(name)
        # print simqueue.item()
        
    while simqueue.size() > 1: # 判断条件，因为最后只能剩下1一个人，所以只要队列长度大于1，就一直循环
        # print simqueue.item()
        
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())  # 不断将队首出列，并入列，其实是在调整位置
            # print simqueue.item()
        simqueue.dequeue()  # 循环num次后彻底将队首出列，意味着这个人被报数点到自己
        
    return simqueue.dequeue() # 返回最后剩下的那个人（元素）

```

双端队列
---

其实就是既可以从队首出列，入列，也可以从队尾出列入列的数据结构

#### 代码

```
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append((item))

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

```


#### 拓展

- 回文问题

其实就是将元素入列后，分别从队首/队尾出列，比较元素是不是相同，直到最后队列中剩下一个或者没有元素即为回文


```
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        #print '1'
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual


print palchecker('asdsa')
print palchecker("radar")
print palchecker("lalksjfklasdjf")
# s = "a,b. d"

```

二叉树
---
python去实现二叉树的话，主要是需要一个节点类作为节点，然后一个树类。
代码如下

```
class BiNode(object):  # 结点类
    def __init__(self, element=None, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def get_element(self):
        return self.element

    def dict_form(self):
        dict_set = {
            "element": self.element,
            "left": self.left,
            "right": self.right,
        }

        return dict_set

    def __str__(self):
        return str(self.element)


class BiTree1(object):  # 树 一颗完全二叉树（意思是一直从左到右添加，除了最后一层，之前的都是满的，可以不为满，但节点要集中在左边）
    def __init__(self, tree_node=None):
        self.root = tree_node

    def add_node_in_order(self, item=None):
        node = BiNode(item)

        if not self.root:
            self.root = node

        else:
            node_queue = []
            node_queue.append(self.root)
            while len(node_queue):
                q_node = node_queue.pop(0)
                if q_node.left is None:
                    q_node.left = node
                    break
                elif q_node.right is None:
                    q_node.right = node
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)
```


#### 构造二叉树

- 通过列表对树进行顺序构造


```
    def set_up_in_order(self,element_list):  # 通过列表对树进行顺序构造
        for elements in element_list:
            self.add_node_in_order(elements)

```

- 通过字典对树构造

```

    def set_up_from_dict(self, dict_instance):
        if not isinstance(dict_instance, dict):
            return None
        else:
            dict_queue = list()
            node_queue = list()
            node = BiNode(dict_instance["element"])
            self.root = node

            node_queue.append(node)
            dict_queue.append(dict_instance)

            while len(dict_queue):
                dict_in = dict_queue.pop(0)
                node = node_queue.pop(0)

                if isinstance(dict_in.get("left", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("left", None), dict):
                        dict_queue.append(dict_in.get("left", None))
                        left_node = BiNode(dict_in.get("left", None)["element"])
                        node_queue.append(left_node)

                    else:
                        left_node = BiNode(dict_in.get("left", None))
                    node.left = left_node

                    if isinstance(dict_in.get("right", None), (dict, int, float, str)):
                        if isinstance(dict_in.get("right", None), dict):
                            dict_queue.append(dict_in.get("right", None))
                            right_node = BiNode(dict_in.get("right", None)["element"])
                            node_queue.append(right_node)

                        else:
                            right_node = BiNode(dict_in.get("right", None))

                        node.right = right_node


```

- 获取深度


```
    def get_depth(self):
        if self.root is None:
            return 0

        else:
            node_queue = list()
            node_queue.append(self.root)
            depth = 0
            while len(node_queue):
                q_len = len(node_queue)

                while q_len:
                    q_node = node_queue.pop(0)
                    q_len = q_len - 1

                    if q_node.left is not None:
                        node_queue.append(q_node.left)
                    if q_node.right is not None:
                        node_queue.append(q_node.right)

                depth = depth + 1

            return depth

```
- 前中后序遍历



```
# 前序遍历

# 1. 如果树为空，返回None 。
# 2. 从根结点开始，如果当前结点左子树存在，则打印结点，并将该结点入栈。让当前结点指向左子树，继续步骤2直至当前结点左子树不存在。
# 3. 将当结点打印出来，如果当前结点的右子树存在，当前结点指向右子树，继续步骤2。否则进行步骤4.
# 4. 如果栈为空则遍历结束。若非空，从栈里面pop一个节点，从当前结点指向该结点的右子树。如果右子树存在继续步骤2，不存在继续步骤4直至结束。
    def pre_traversal(self):
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root

            while node is not None or len(node_stack):
                if node is None:
                    node = node_stack.pop().right
                    continue

                while node.left is not None:
                    node_stack.append(node)
                    output_list.append(node.get_element())
                    node = node.left

                output_list.append(node.get_element())
                node = node.right
        return output_list

# 中序

    def in_traversal(self):
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root

            while node is not None or len(node_stack):
                if node is None:
                    node = node_stack.pop()
                    output_list.append(node.get_element())
                    node = node.right

                while node.left is not None:
                    node_stack.append(node)
                    node = node.left

                output_list.append(node.get_element())
                node = node.right

        return output_list


# 后序
    def post_traversal(self):
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root

            while node is not None or len(node_stack):
                if node is None:
                    node = node_stack.pop().left

                while node.right is not None:
                    node_stack.append(node)
                    output_list.append(node.get_element())
                    node = node.right
                output_list.append(node.get_element())
                node = node.left

        return output_list[::-1]

# 更简单的递归写法

# 依次为前中后遍历
    def preOrder(self, BinaryTreeNode):
        if BinaryTreeNode is None:
            return
        # 先打印根结点，再打印左结点，后打印右结点
        print(BinaryTreeNode.data)
        self.preOrder(BinaryTreeNode.left)
        self.preOrder(BinaryTreeNode.right)

    def inOrder(self, BinaryTreeNode):
        if BinaryTreeNode is None:
            return
        # 先打印左结点，再打印根结点，后打印右结点
        self.inOrder(BinaryTreeNode.left)
        print(BinaryTreeNode.data)
        self.inOrder(BinaryTreeNode.right)

    def postOrder(self, BinaryTreeNode):
        if BinaryTreeNode is None:
            return
        # 先打印左结点，再打印右结点，后打印根结点
        self.postOrder(BinaryTreeNode.left)
        self.postOrder(BinaryTreeNode.right)
        print(BinaryTreeNode.data)

```
