# -*- coding: utf-8 -*-
# @File  : diameter_of_binary_tree.py
# @Author: tao.gan@advance.ai
# @Date  : 2020-07-07
# @Desc  :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self._max_high = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def high(root: TreeNode) -> int:
            if root is None:
                return 0

            left = high(root.left)
            right = high(root.right)
            self._max_high = max(self._max_high, left + right)
            return max(left, right) + 1
        high(root)
        return self._max_high


def main():
    test_cases = [
        TreeNode(1, TreeNode(2, TreeNode(TreeNode(4), TreeNode(5))), TreeNode(3))
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.diameterOfBinaryTree(test_case))


if __name__ == '__main__':
    main()