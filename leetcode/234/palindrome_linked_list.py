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
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]


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


if __name__ == '__main__':
    main()
