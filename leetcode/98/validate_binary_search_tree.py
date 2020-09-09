# -*- coding: utf-8 -*-
# @File  : validate_binary_search_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-09
# @Desc  :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is not None:
            if root.val >= root.left.val:
                return False
            else:
                self.isValidBST(root.left)
        if root.right is not None:
            if root.val <= root.right.val:
                return False
            else:
                self.isValidBST(root.right)


def main():
    tree1 = TreeNode(2)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(5)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(4)
    tree2.right.left = TreeNode(3)
    tree2.right.right = TreeNode(6)

    test_cases = [tree1, tree2]
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.isValidBST(test_case))


if __name__ == '__main__':
    main()
