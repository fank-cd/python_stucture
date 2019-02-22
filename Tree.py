# coding:utf-8


class Node(object):  # 结点类
    def __init__(self, data=None, l_child=None, r_child=None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child


class B_Tree1(object):  # 树 一颗完全二叉树（意思是一直从左到右添加，除了最后一层，之前的都是满的，可以不为满，但节点要集中在左边）
    def __init__(self, node=None):
        self.root = node

    def add(self, item=None):
        node = Node(item)

        if not self.root:
            self.root = node

        else:
            my_queue = []
            my_queue.append(self.root)

            while True:
                cur_node = my_queue.pop(0)
                if not cur_node.l_child:
                    cur_node.l_child = node
                    return
                elif not cur_node.r_child:
                    cur_node.r_child = node
                    return

                else:
                    my_queue.append(cur_node.l_child)
                    my_queue.append(cur_node.r_child)


class B_Tree2(object):  # 树
    def __init__(self, node=None):
        self.root = node

    def add(self, item=None):
        node = Node(data=item)

        if not self.root or self.root.data is None: # 我怀疑这个条件是一回事呢
            self.root = node

        else:
            my_queue = []
            my_queue.append(self.root)
            while True:
                cur_node = my_queue.pop(0)
                if cur_node.data is None:
                    continue
                if not cur_node.l_child:
                    cur_node.l_child = node
                    return
                elif not cur_node.r_child:
                    cur_node.r_child = node
                    return
                else:
                    my_queue.append(cur_node.l_child)
                    my_queue.append(cur_node.r_child)


    # 层次遍历
    def floor_travel(self):
        if not self.root or self.root.data is None:
            return []

        else:
            my_queue = []
            re_queue = []

            my_queue.append(self.root)

            while my_queue:
                cur_node = my_queue.pop(0)
                re_queue.append(cur_node)
                if cur_node.l_child:
                    my_queue.append(cur_node.l_child)
                if cur_node.r_child:
                    my_queue.append(cur_node.r_child)

            return re_queue




def main():
    # 创建一个二叉树对象
    tree = B_Tree2()
    # 以此向树中添加节点，i == 3的情况表示，一个空节点，看完后面就明白了
    for i in range(10):
        if i == 3:
            i = None
        tree.add(i)
    #广度优先的层次遍历算法
    print([i.data for i in tree.floor_travel()])
    #前，中，后序 遍历算法（递归实现）
    print([i.data for i in tree.front_travel()])
    print([i.data for i in tree.middle_travel()])
    print([i.data for i in tree.back_travel()])
    print('------------------------------------')
    #前，中，后序 遍历算法（堆栈实现）
    print([i.data for i in tree.front_stank_travel()])
    print([i.data for i in tree.middle_stank_travel()])
    print([i.data for i in tree.back_stank_travel()])

if __name__ == "__main__":
    main()