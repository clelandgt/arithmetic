# -*- coding: utf-8 -*-
# @File  : sum_numbers.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-29
# @Desc  :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def sumNumbers(self, root: TreeNode) -> int:
        global total
        total = 0

        def _sum_number(tree_node, num=0):
            global total
            if tree_node.left is None and tree_node.right is None:
                total += num
                return

            num = num * 10 + tree_node.val
            if tree_node.left is not None:
                _sum_number(tree_node.left, num)

            if tree_node.right is not None:
                _sum_number(tree_node.right, num)
        _sum_number(root, 0)

        return total


def main():
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(3)

    node2 = TreeNode(1)
    node22 = TreeNode(9)
    node22.left = TreeNode(5)
    node22.right = TreeNode(1)
    node2.left = node22
    node2.right = TreeNode(0)

    test_cases = [
        node1,
        node2
    ]

    s1 = Solution1()
    for test_case in test_cases:
        print(s1.sumNumbers(test_case))


if __name__ == '__main__':
    main()
