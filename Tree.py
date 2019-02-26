# coding:utf-8


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

    def set_up_in_order(self,element_list):  # 通过列表对树进行顺序构造
        for elements in element_list:
            self.add_node_in_order(elements)

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


# 1. 如果树为空，返回0 。
# 2. 从根结点开始，将根结点拉入列。
# 3. 当列非空，记当前队列元素数（上一层节点数）。将上层节点依次出队，如果左右结点存在，依次入队。直至上层节点出队完成，
# 深度加一。继续第三步，直至队列完全为空
#

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

# 前序遍历

# 1. 如果树为空，返回None 。
# 2. 从根结点开始，如果当前结点左子树存在，则打印结点，并将该结点入栈。让当前结点指向左子树，继续步骤2直至当前结点左子树不存在。
# 3. 将当结点打印出来，如果当前结点的右子树存在，当前结点指向右子树，继续步骤2。否则进行步骤4.
# 4. 如果栈为空则遍历结束。若非空，从栈里面pop一个节点，从当前结点指向该结点的右子树。如果右子树存在继续步骤2，不存在继续步骤4直至结束。



# 用字典构造二叉树
"""
dict_tree = { 
    "element": 0, 
    "left": { 
            "element": 1, 
            "left": { 
                "element": 3, 
                "left": 6, 
                "right": 7, 
                    } 
            }, 
    "right": { 
            "element": 2, 
            "left": 4, 
            "right": { 
                "element": 5, 
                "left": 8, 
                "right": 9,
                        },
            }, 
}

"""
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

