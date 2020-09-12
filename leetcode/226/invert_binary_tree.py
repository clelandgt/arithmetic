# -*- coding: utf-8 -*-
# @File  : invert_binary_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-12
# @Desc  :
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.root = None

    def invertTree(self, root: TreeNode) -> TreeNode:
        if self.root is None:
            self.root = root
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return self.root


class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


def main():
    tree1 = TreeNode(4)
    tree1.left = TreeNode(2, TreeNode(1), TreeNode(3))
    tree1.right = TreeNode(7, TreeNode(6), TreeNode(9))

    test_cases = [
        copy.deepcopy(tree1)
    ]
    s1 = Solution1()
    for test_case in test_cases:
        node = s1.invertTree(test_case)
        pass

    test_cases = [
        copy.deepcopy(tree1)
    ]
    s2 = Solution2()
    for test_case in test_cases:
        node = s2.invertTree(test_case)
        pass


if __name__ == '__main__':
    main()
