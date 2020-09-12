# -*- coding: utf-8 -*-
# @File  : flatten_binary_tree_to_linked_list.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-12
# @Desc  : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
import graphviz


class TreeNode:
    def __init__(self, val=0, left=None , right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.current_node = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.current_node = root
        self.flatten(root.left)


def main():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    tree1.right = TreeNode(5, None, TreeNode(6))
    print(graphviz.Source(tree1))

    test_cases = [tree1]




if __name__ == '__main__':
    main()
