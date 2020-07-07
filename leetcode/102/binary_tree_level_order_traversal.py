# -*- coding: utf-8 -*-
# @File  : binary_tree_level_order_traversal.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-07
# @Desc  :
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """层层遍历
    易错点: 一定要保持原有顺序
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        result, level = [], [root]
        while level:
            result.append([item.val for item in level])
            temp = []
            for item in level:
                temp.extend([item.left, item.right])
            level = [item for item in temp if item is not None]

        return result


def main():
    # [3, 9, 20, null, null, 15, 7]

    test_cases = [
        TreeNode(3, TreeNode(9, None), TreeNode(20, TreeNode(15, None), TreeNode(7, None)))
    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.levelOrder(test_case))


if __name__ == '__main__':
    main()