# -*- coding: utf-8 -*-
# @File  : merge_two_binary_trees.py
# @Author: clelandgt@163.com
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
        self.result = TreeNode(0)

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(current: TreeNode, t1: TreeNode, t2: TreeNode) -> TreeNode:
            if t1 is None and t2 is None:
                return
            t1_val = t1.val if t1 is not None else 0
            t2_val = t2.val if t2 is not None else 0
            current.val = t1_val + t2_val

            merge(current.left, t1.left, t2.left)
            merge(current.right, t1.right, t2.right)

        merge(self.result, t1, t2)
        return self.result


def main():
    test_cases = [
        {'tree1': TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)), 'tree2': TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))}
    ]

    print('Solution1')
    for test_case in test_cases:
        s1 = Solution1()
        s1.mergeTrees(test_case['tree1'], test_case['tree2'])
        print(s1)


if __name__ == '__main__':
    main()
