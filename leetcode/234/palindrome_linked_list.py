# -*- coding: utf-8 -*-
# @File  : palindrome_linked_list.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-30
# @Desc  :
"""
回文数: 若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数.
n1=1234321, n=123321 都是回文数
"""
from copy import deepcopy


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
    """ 遍历链表到数组里，然后使用双指针分别从两端向中间遍历比较
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1

        return True


class Solution3:
    """ 快慢指针 + 反转链表
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def reverse_link(self, head):
        if head is None or head.next is None:
            return head
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        # 遍历到中端位置
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反转后半段链表
        current_node = self.reverse_link(slow)

        # 比较前与后半段
        p = head
        while p and current_node:
            if p.val != current_node.val:
                return False
            p = p.next
            current_node = current_node.next

        return True


class Solution4:
    """ 快慢指针 + 栈
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        slow, fast = head, head
        stack = [slow.val]
        # 遍历到中间节点, slow入栈节点数据
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast.next:
                stack.append(slow.val)

        # slow后续遍历的数据等于之前入栈的数据
        slow = slow.next
        while slow:
            num = stack.pop()
            if slow.val != num:
                return False
            slow = slow.next
        return True


def main():
    test_cases = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))),
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1)))))),
        ListNode(1, ListNode(2)),
        ListNode(1, ListNode(0, ListNode(0))),
        ListNode(1),
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        print(s.isPalindrome(deepcopy(test_case)))

    print('Solution2')
    s = Solution2()
    for test_case in test_cases:
        print(s.isPalindrome(deepcopy(test_case)))

    print('Solution3')
    s = Solution3()
    for test_case in test_cases:
        print(s.isPalindrome(deepcopy(test_case)))

    print('Solution4')
    s = Solution4()
    for test_case in test_cases:
        print(s.isPalindrome(deepcopy(test_case)))


if __name__ == '__main__':
    main()
