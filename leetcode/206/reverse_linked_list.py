# -*- coding: utf-8 -*-
# @File  : reverse_linked_list.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-30
# @Desc  :
from copy import deepcopy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """ 双指针
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def print_links(self, head: ListNode) -> None:
        p = head
        while p:
            if p.next:
                print(p.val, end='->')
            else:
                print(p.val)
            p = p.next
        print('\n')


class Solution2:
    """ 递归实现
    先递到 head.next=null, 再归时做反转链表
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def print_links(self, head: ListNode) -> None:
        p = head
        while p:
            if p.next:
                print(p.val, end='->')
            else:
                print(p.val)
            p = p.next
        print('\n')


def main():
    # Input: 1->2->3->4->5->NULL
    # Output: 1<-2<-3<-4<-5<-NULL
    test_cases = [
        None,
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(None))))))
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        result = s1.reverseList(deepcopy(test_case))
        s1.print_links((result))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        result = s2.reverseList(deepcopy(test_case))
        s2.print_links((result))


if __name__ == '__main__':
    main()
