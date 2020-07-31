# -*- coding: utf-8 -*-
# @File  : kth_smallest_element_in_bst.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-31
# @Desc  :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.__k = 0
        self.__res = None

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.__k = k

        def _kth_smallest(root):
            if root == None:
                return

            _kth_smallest(root.left)
            self.__k -= 1
            if self.__k == 0:
                self.__res = root.val
                return
            _kth_smallest(root.right)

        _kth_smallest(root)
        return self.__res


def main():
    test_cases = [
        (TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1),
        (TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3)
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
       print( s1.kthSmallest(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
