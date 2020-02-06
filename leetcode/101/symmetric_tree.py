# -*- coding: utf-8 -*-
# @File  : symmetric_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-04
# @Desc  :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """未实现"""
    def __init__(self):
        self._in_nums = []

    def isSymmetric(self, root: TreeNode) -> bool:
        self.root = root
        self.in_order()

        nums = self._in_nums
        midile = int((len(nums)+1)/2)
        print(len(nums))
        for index in range(0, midile):
            if nums[index] != nums[len(nums)-1-index]:
                return False
        return True

    def in_order(self):
        """ 中序遍历
        inOrder(r->left)->r->inOrder(r->right)
        :return:
        """
        self._in_nums = []
        self._in_order(self.root)
        return self._in_nums

    def _in_order(self, node: TreeNode):
        if node is None:
            return

        self._in_order(node.left)
        self._in_nums.append(node.val)
        self._in_order(node.right)


class Solution2:
    """ 递归分治将问题规模减低
    参考：https://leetcode.com/problems/symmetric-tree/solution/
    手画图: https://cleland.oss-cn-beijing.aliyuncs.com/leetcode/101/leetcode_101_01.jpeg

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def __init__(self):
        pass

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, node1: TreeNode, node2: TreeNode):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False

        return node1.val == node2.val and self.is_mirror(node1.left, node2.right) and self.is_mirror(node1.right, node2.left)


class Solution3:
    def __init__(self):
        pass

    def isSymmetric(self, root: TreeNode) -> bool:
        pass


def main():
    # tree = TreeNode(1)
    # tree.left = TreeNode(2)
    # tree.right = TreeNode(2)
    # tree.left.left = TreeNode(3)
    # tree.left.right = TreeNode(4)
    # tree.right.left = TreeNode(4)
    # tree.right.right = TreeNode(3)

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(2)
    tree.left.right = None
    tree.right.left = TreeNode(2)

    s = Solution2()
    print(s.isSymmetric(tree))


if __name__ == '__main__':
    main()
