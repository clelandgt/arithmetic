# -*- coding: utf-8 -*-
# @File  : merge_two_sorted_lists.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-27
# @Desc  :


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_link(head: ListNode):
    p = head
    while p:
        if p.next:
            print(p.val, end='->')
        else:
            print(p.val, end='')
        p = p.next
    print('\n')


class Solution1:
    """
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(1)
        p = head
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    p.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    p.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1 and not l2:
                p.next = l1
                break
            elif not l1 and l2:
                p.next = l2
                break
            p = p.next

        return head.next


class Solution2:
    """
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(1)
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next

        if l1 is not None and l2 is None:
            p.next = l1
        if l1 is None and l2 is not None:
            p.next = l2

        return head.next


def main():
    # 1->2->4, 1->3->5->6->7
    test_cases = [
        {'l1': ListNode(1, ListNode(2, ListNode(4))), 'l2': ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(7)))))},
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        tmp_link = s.mergeTwoLists(test_case['l1'], test_case['l2'])
        print_link(tmp_link)

    print('Solution2')
    s = Solution2()
    for test_case in test_cases:
        tmp_link = s.mergeTwoLists(test_case['l1'], test_case['l2'])
        print_link(tmp_link)


if __name__ == '__main__':
    main()

