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
    def __init__(self):
        self.total = 0

    def sumNumbers(self, root: TreeNode) -> int:
        """深度优先搜索
        时间复杂度: O(n)
        空间复杂度: O(n)
        """

        def _sum_number(tree_node, num=0):
            num = num * 10 + tree_node.val

            if tree_node.left is None and tree_node.right is None:
                self.total += num
                return

            if tree_node.left is not None:
                _sum_number(tree_node.left, num)

            if tree_node.right is not None:
                _sum_number(tree_node.right, num)

        if root:
            _sum_number(root, 0)

        return self.total


class Solution2:
    """深度优先搜索(改进)
    时间复杂度: O(n)
    空间复杂度: O(n)
    """

    def sumNumbers(self, root: TreeNode) -> int:
        def _sum_number(tree_node, num=0):
            if tree_node is None:
                return 0
            total = num * 10 + tree_node.val
            if tree_node.left is None and tree_node.right is None:
                return total
            return _sum_number(tree_node.left, total) + _sum_number(tree_node.right, total)

        return _sum_number(root, 0)


def main():
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(3)

    node2 = TreeNode(4)
    node22 = TreeNode(9)
    node22.left = TreeNode(5)
    node22.right = TreeNode(1)
    node2.left = node22
    node2.right = TreeNode(0)

    test_cases = [
        node1,
        node2
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.sumNumbers(test_case))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.sumNumbers(test_case))


if __name__ == '__main__':
    main()
