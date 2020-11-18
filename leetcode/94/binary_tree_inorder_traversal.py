# -*- coding: utf-8 -*-
# @File  : binary_tree_inorder_traversal.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-27
# @Desc  :

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """ 递归遍历
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def __init__(self):
        self.__result = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def _inorderTraversal(root):
            if not root:
                return
            _inorderTraversal(root.left)
            self.__result.append(root.val)
            _inorderTraversal(root.right)
        _inorderTraversal(root)
        return self.__result


def main():
    test_cases = [
        TreeNode(1, None, TreeNode(2, TreeNode(3))),
        None,
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        print(s.inorderTraversal(test_case))


if __name__ == '__main__':
    main()
