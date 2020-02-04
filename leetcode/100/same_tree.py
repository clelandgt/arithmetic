# -*- coding: utf-8 -*-
# @File  : same_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-03
# @Desc  : https://leetcode.com/problems/same-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        选择前序遍历的方式一一比较
        :param p:
        :param q:
        :return:
        """
        return self.pre_order(p, q)

    def pre_order(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False
        else:
            return self.pre_order(node1.left, node2.left) & self.pre_order(node1.right, node2.right)


def main():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    s = Solution1()
    print(s.isSameTree(tree1, tree2))


if __name__ == '__main__':
    main()