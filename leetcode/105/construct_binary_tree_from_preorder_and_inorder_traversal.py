# -*- coding: utf-8 -*-
# @File  : construct_binary_tree_from_preorder_and_inorder_traversal.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-11
# @Desc  :

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """超时了"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder is None or len(inorder) == 0:
            return
        ind = inorder.index(preorder.pop(0))
        in_left = inorder[:ind]
        in_right = inorder[ind+1:]
        pre_left = [item for item in preorder if item in in_left]
        pre_right = [item for item in preorder if item in in_right]

        root = TreeNode(inorder[ind])
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root


def main():
    test_cases = [
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]]
    ]
    s1 = Solution1()
    for test_case in test_cases:
        tree1 = s1.buildTree(test_case[0], test_case[1])
        pass


if __name__ == '__main__':
    main()
