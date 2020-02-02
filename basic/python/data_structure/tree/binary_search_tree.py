# -*- coding: utf-8 -*-
# @File  : binary_search_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-01
# @Desc  :
from . import Node, BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super(__class__, self).__init__()

    def insert(self, value):
        """ 插入数据
        1. 如头节点为空，插入头节点。
        2. 如果比当前节点小，则查找左子节点树，否则查找右子节点树。递归遍历，直到某个子节点为空时，插入数据。
        :param value:
        :return:
        """
        if not self.root:
            self.root = Node(value)
            return
        return self._insert1(self.root, value)
        #return self._insert2(value)

    def _insert1(self, node: Node, value):
        """ 递归的方式实现

        :param node:
        :param value:
        :return:
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            else:
                self._insert1(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                return
            else:
                self._insert1(node.right, value)

    def _insert2(self, value):
        """ 循环的方式实现

        :param node:
        :param value:
        :return:
        """
        if self.root is None:
            self.root = Node(value)
            return

        cur_node = self.root
        while True:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = Node(value)
                    return
                else:
                    cur_node = cur_node.left
            elif value > cur_node.value:
                if cur_node.right is None:
                    cur_node.right = Node(value)
                    return
                else:
                    cur_node = cur_node.right

    def delete(self, value):
        pass

    def find(self, value):
        """ 查找数据
        查找数据小于当前节点数据，遍历左子节点树；否则遍历右子节点树。直到节点为空或节点的数据等于查找数据。
        :param value:
        :return:
        """
        return self._find1(self.root, value)
        # return self._find2(value)

    def _find1(self, node: Node, value):
        """ 递归方式实现 """
        if node is None:
            return

        if value == node.value:
            return node
        elif value < node.value:
            return self._find1(node.left, value)
        else:
            return self._find1(node.right, value)

    def _find2(self, value):
        """ 循环的方式实现 """
        cur_node = self.root

        while cur_node:
            if value == cur_node.value:
                return cur_node
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

    def pre_order(self):
        """ 前序遍历
        r->preOrder(r->left)->preOrder(r->right)
        :return:
        """
        self._pre_nums = []
        self._pre_order(self.root)
        return self._pre_nums

    def _pre_order(self, node: Node):
        if node is None:
            return

        self._pre_nums.append(node.value)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def in_order(self):
        """ 中序遍历
        inOrder(r->left)->r->inOrder(r->right)
        :return:
        """
        pass

    def post_order(self):
        """ 后序遍历
        postOrder(r->left)->postOrder(r->right)->r
        :return:
        """
        pass


def main():
    u""" 构建的基础二叉树
                  13
                /   / \
              10   14 16
              / \      \
             9  11     17
            /
           8
    """

    tree = BinarySearchTree()

    # 1. 插入数据，构建搜索二叉树
    tree.insert(13)
    tree.insert(10)
    tree.insert(16)
    tree.insert(9)
    tree.insert(11)
    tree.insert(14)
    tree.insert(17)
    tree.insert(8)

    # 2. 查找
    print('find 10 in binary tree: ', tree.find(10).value)

    # 3. 删除

    # 4. 遍历(前、中、后序)
    print('pre order: ', tree.pre_order())

    min_value = tree.get_min()
    print('trees min value: {}'.format(min_value))

    max_value = tree.get_max()
    print('trees max value: {}'.format(max_value))

    # result = tree.find(10)
    # print('find 10 in tree, result: {}'.format(result.value))
    #
    # print(u'前序遍历:')
    # tree.pre_order(tree.root)
    #
    # print(u'中序遍历:')
    # tree.in_order(tree.root)
    #
    # print(u'后序遍历:')
    # tree.bac_order(tree.root)
