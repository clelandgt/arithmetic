# -*- coding: utf-8 -*-
# @File  : validate_binary_search_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-09
# @Desc  :
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        r1, r2 = True, True
        if root is None:
            return True
        if root.left is not None:
            if root.left.val >= root.val:
                return False
            else:
                r1 = self.isValidBST(root.left)
        if root.right is not None:
            if root.right.val <= root.val:
                return False
            else:
                r2 = self.isValidBST(root.right)

        if r1 is False or r2 is False:
            return False
        else:
            return True


class Solution2:
    def isValidBST(self, root: TreeNode,
                   max_root_val: int = sys.maxsize,
                   min_root_val: int = -sys.maxsize) -> bool:
        if root:
            # The current node must not statisfy any of the conditions
            if root.val >= max_root_val or root.val <= min_root_val:
                return False
            else: # Check left-subtree and right-subtree
                return (self.isValidBST(root.left, min(max_root_val, root.val), min_root_val)
                        and self.isValidBST(root.right, max_root_val, max(min_root_val, root.val)))
        else: # By default return true
            return True


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
    s1 = Solution2()
    for test_case in test_cases:
        print(s1.isValidBST(test_case))


if __name__ == '__main__':
    main()
