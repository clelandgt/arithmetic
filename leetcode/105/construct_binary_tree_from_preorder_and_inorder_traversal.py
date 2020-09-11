# -*- coding: utf-8 -*-
# @File  : construct_binary_tree_from_preorder_and_inorder_traversal.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-11
# @Desc  :
from collections import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass



def main():
    test_cases = [
        [[3,9,20,15,7], [9,3,15,20,7]]
    ]


if __name__ == '__main__':
    main()
