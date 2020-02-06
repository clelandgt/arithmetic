# -*- coding: utf-8 -*-
# @File  : max_deep_binary_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-06
# @Desc  : https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """ 深度递归遍历
    时间复杂度: O(n)
    空间复杂度：O(n)

    """
    def __init__(self):
        self._max_deep = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.recursion(root, 0)
        return self._max_deep

    def recursion(self, node: TreeNode, cur_deep):
        if not node:
            if cur_deep > self._max_deep:
                self._max_deep = cur_deep
            return

        cur_deep += 1
        self.recursion(node.left, cur_deep)
        self.recursion(node.right, cur_deep)


def main():

    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    # tree.right.left.left = TreeNode(12)
    # tree.right.left.right = TreeNode(13)

    s1 = Solution1()
    print(s1.maxDepth(tree))


if __name__ == '__main__':
    main()