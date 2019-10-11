# -*- coding: utf-8 -*-
# @File  : binary_search_tree.py
# @Author: Cleland
# @Date  : 2019/3/1
# @Desc  : 二叉搜索树(BST)
from . import Node


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self._pre_order = []
        self._in_order = []
        self._bac_order = []

    def insert(self, value):
        """ 插入
        1. 如果头结点为空插入头节点
        2. 数据比当前节点大，遍历子节点树。反之遍历右节点树。递归遍历，直到某个节点的子节点为空时，插入数据。
        :param value:
        :return:
        """
        if self.root is None:
            self.root = Node(value)
            return

        cur_node = self.root
        while cur_node:
            if value < cur_node.value:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(value)
                    return
            elif value > cur_node.value:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(value)
                    return

    def find(self, value):
        """ 查找数据
        查找数据小于当前节点，遍历左子节点树，反之遍历右节点树。递归遍历，知道遍历到数据与节点数据相等，或是遍历完树，都没找到。
        :param value:
        :return: 定位到数据时，返回该节点，否则返回为空。
        """
        cur_node = self.root
        while cur_node:
            if value == cur_node.value:
                return cur_node
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

    def delete(self, value):
        """ 删除数据
        头结点为空直接放回，不为空时，有以下几种可能：
        1. 删除的节点，没有左右子树，直接删除该节点；
        2. 删除的节点，只有左或右子树，直接使用不为空的子节点替换删除节点。
        3. 删除的节点，有左右子树，遍历右子树的最小节点替换删除节点。

        :param value:
        :return:
        """

        cur_node = self.root
        if not cur_node:
            return

        # 定位查找的数据
        parent_node = cur_node
        while cur_node:
            parent_node = cur_node
            if value == cur_node.value:
                break
            elif value > cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        if parent_node == cur_node:
            cur_node = None

        # 删除节点
        # 没有左右子树
        if (cur_node.left is None) and (cur_node.right is None):
            parent_node.le

        # 只有左或右子树
        if (cur_node.left is not None) and (cur_node.right is None):
            parent_node.left = cur_node.left
            del cur_node
        elif (cur_node.left is None) and (cur_node.right is not None):
            parent_node.right = cur_node.right
            del cur_node

    def get_min(self):
        """ 返回最小值

        :return:
        """
        min_value = None
        cur_code = self.root

        while cur_code:
            min_value = cur_code.value
            cur_code = cur_code.left
        return min_value

    def get_min_node(self):
        """ 返回最小值节点

        :return:
        """
        min_node = None
        cur_code = self.root

        while cur_code:
            min_node = cur_code
            cur_code = cur_code.left
        return min_node

    def get_max(self):
        """ 返回最大值

        :return:
        """
        max_value = None
        cur_code = self.root

        while cur_code:
            max_value = cur_code.value
            cur_code = cur_code.right
        return max_value

    def get_max_node(self):
        """ 返回最大值

        :return:
        """
        max_node = None
        cur_code = self.root

        while cur_code:
            max_node = cur_code
            cur_code = cur_code.right
        return max_node

    def pre_order(self, node):
        """ 前序遍历
        根节点 -> 左子节点 -> 右子节点
        :return:
        """
        if not node:
            return
        print (node.value)
        self._pre_order.append(node)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        """ 中序遍历
        左子节点 -> 当前节点 -> 右子节点
        :return:
        """
        if not node:
            return
        self.in_order(node.left)
        print (node.value)
        self._in_order.append(node)
        self.in_order(node.right)

    def bac_order(self, node):
        """ 后序遍历
        左子节点 -> 右子节点 -> 当前节点
        :return:
        """
        if not node:
            return
        self.bac_order(node.left)
        self.bac_order(node.right)
        print (node.value)
        self._bac_order.append(node)

    def bfs(self):
        """ 广度优先遍历(借助队列)

        :return:
        """
        # TODO: 待补充
        raise NotImplementedError

    def dfs(self):
        """ 深度优先遍历(借助栈)

        :return:
        """
        # TODO: 待补充
        raise NotImplementedError


def test():
    tree = BinarySearchTree()
    tree.insert(13)
    tree.insert(10)
    tree.insert(16)
    tree.insert(9)
    tree.insert(11)
    tree.insert(14)
    tree.insert(17)
    tree.insert(8)


    """
                  13
                /  / \
              10   14 16
              / \      \   
             9  11     17
            /    
           8     
    """

    min_value = tree.get_min()
    print ('trees min value: {}'.format(min_value))

    max_value = tree.get_max()
    print ('trees max value: {}'.format(max_value))

    result = tree.find(10)
    print ('find 10 in tree, result: {}'.format(result.value))

    print (u'前序遍历:')
    tree.pre_order(tree.root)

    print (u'中序遍历:')
    tree.in_order(tree.root)

    print (u'后序遍历:')
    tree.bac_order(tree.root)
