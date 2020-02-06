# -*- coding: utf-8 -*-
# @File  : mini_depth_binary_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-06
# @Desc  :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """ 深度递归遍历
    未成功
    时间复杂度: O(n)
    空间复杂度：O(n)

    """
    def __init__(self):
        # min_deep初始化为最大值
        self._min_deep = float('inf')

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            self._min_deep = 0
        self.recursion(root, 0)
        return self._min_deep

    def recursion(self, node: TreeNode, cur_deep):
        if not node:
            if cur_deep < self._min_deep:
                self._min_deep = cur_deep
            return

        cur_deep += 1
        self.recursion(node.left, cur_deep)
        self.recursion(node.right, cur_deep)


class Solution2:
    """ 深度递归遍历
    时间复杂度: O(n)
    空间复杂度：O(n)

    """
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1
        elif root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


def main():
    # tree非空测试
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    tree.right.left.left = TreeNode(12)
    tree.right.left.right = TreeNode(13)

    # tree为空测试
    # tree = None

    # 测试失败的案例1，重跑
    tree = TreeNode(1)
    tree.left = TreeNode(2)

    s1 = Solution2()
    print(s1.minDepth(tree))


if __name__ == '__main__':
    main()