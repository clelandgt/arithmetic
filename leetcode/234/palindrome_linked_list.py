# -*- coding: utf-8 -*-
# @File  : palindrome_linked_list.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-30
# @Desc  :
"""
回文数: 若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数.
n1=1234321, n=123321 都是回文数
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]


class Solution2:
    """
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        # 遍历到中端位置
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反转后半段链表
        current_node = None
        last_node = None
        p = slow
        while p:
            current_node = ListNode(p.val, last_node)
            last_node = current_node
            p = p.next

        # 比较前与后半段
        p = head
        while p and current_node:
            if p.val != current_node.val:
                return False
            p = p.next
            current_node = current_node.next

        return True


def main():
    test_cases = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))),
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1)))))),
        ListNode(1, ListNode(2)),
        ListNode(1),
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        print(s.isPalindrome(test_case))

    print('Solution2')
    s = Solution2()
    for test_case in test_cases:
        print(s.isPalindrome(test_case))


if __name__ == '__main__':
    main()
