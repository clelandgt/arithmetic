# -*- coding: utf-8 -*-
# @File  : flatten_binary_tree_to_linked_list.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-12
# @Desc  : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class TreeNode:
    def __init__(self, val=0, left=None , right=None):
        self.val = val
        self.left = left
        self.right = right


# 这里Solution1存在问题，虽然第一想法是前序遍历来形成构成链表，会比较麻烦，构建时，会破坏左右子节点。从另一个角度，从后往前构建，这样反转前序遍历来实现。
# class Solution1:
#     def __init__(self):
#         self.current_node = None
#
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if root is None:
#             return
#         self.current_node = root
#         self.flatten(root.left)
#         tmp = root.right
#         root.right = root.left
#         root.left = None
#         self.flatten(tmp)


class Solution1:
    def __init__(self):
        self.pre_node = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)

        root.left = None
        root.right = self.pre_node
        self.pre_node = root


def main():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    tree1.right = TreeNode(5, None, TreeNode(6))

    test_cases = [
        tree1
    ]

    s1 = Solution1()
    for test_case in test_cases:
        s1.flatten(test_case)
        pass




if __name__ == '__main__':
    main()
