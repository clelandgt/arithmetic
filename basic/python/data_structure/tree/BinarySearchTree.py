# -*- coding: utf-8 -*-
# @File  : BinarySearchTree.py
# @Author: Cleland
# @Date  : 2019/3/1
# @Desc  :


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        cur_node = self.root
        while cur_node:
            if data < cur_node.data:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(data)
                    return
            elif data > cur_node.data:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(data)
                    return

    def get_min(self):
        min_data = None
        cur_code = self.root

        while cur_code:
            min_data = cur_code.data
            cur_code = cur_code.left
        return min_data

    def get_max(self):
        max_data = None
        cur_code = self.root

        while cur_code:
            max_data = cur_code.data
            cur_code = cur_code.right
        return max_data


def test():
    tree = BinarySearchTree()
    tree.insert(13)
    tree.insert(10)
    tree.insert(16)
    tree.insert(9)
    tree.insert(11)
    tree.insert(14)

    min_data = tree.get_min()
    print 'trees min value: {}'.format(min_data)

    max_data = tree.get_max()
    print 'trees max value: {}'.format(max_data)


if __name__ == '__main__':
    test()
