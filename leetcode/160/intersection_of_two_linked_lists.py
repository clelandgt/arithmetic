# -*- coding: utf-8 -*-
# @File  : intersection_of_two_linked_lists.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-29
# @Desc  :


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        uniq = set()

        while headA:
            uniq.add((id(headA)))
            headA = headA.next
        while headB:
            if id(headB) in uniq:
               return headB
            headB = headB.next


def main():
    # listA = [4,1,8,4,5], listB = [5,0,1,8,4,5]
    l11 = ListNode(8, ListNode(4, ListNode(5)))
    test_cases = [
        {'l1': ListNode(4, ListNode(1, l11)), 'l2': ListNode(5, ListNode(0, ListNode(1, l11)))}
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        print(s.getIntersectionNode(test_case['l1'], test_case['l2']).val)


if __name__ == '__main__':
    main()
