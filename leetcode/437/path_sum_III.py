# -*- coding: utf-8 -*-
# @File  : path_sum_III.py
# @Author: tao.gan@advance.ai
# @Date  : 2020-07-07
# @Desc  :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        _reuslt = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return
        if root.val



def main():
    test_cases = [
        TreeNode(10,
                 TreeNode(5, TreeNode(TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1)))),
                 TreeNode(-3, None, TreeNode(11))
        )
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.pathSum(test_case, 8))


if __name__ == '__main__':
    main()