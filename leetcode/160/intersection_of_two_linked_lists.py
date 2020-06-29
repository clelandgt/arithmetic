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
    """
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        uniq = set()

        while headA:
            uniq.add((id(headA)))
            headA = headA.next
        while headB:
            if id(headB) in uniq:
               return headB
            headB = headB.next


class Solution2:
    """
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        uniq = set()

        while headA or headB:
            if headA:
                if id(headA) in uniq:
                    return headA
                else:
                    uniq.add(id(headA))
                headA = headA.next

            if headB:
                if id(headB) in uniq:
                    return headB
                else:
                    uniq.add(id(headB))
                headB = headB.next


def main():
    # case1: listA = [4,1,8,4,5], listB = [5,0,1,8,4,5]
    # case2: listA = [0, 9, 1, 2, 4], listB = [3, 2, 4]

    l11 = ListNode(8, ListNode(4, ListNode(5)))
    l22 = ListNode(2, ListNode(4))
    test_cases = [
        {'l1': ListNode(4, ListNode(1, l11)), 'l2': ListNode(5, ListNode(0, ListNode(1, l11)))},
        {'l1': ListNode(0, ListNode(9, ListNode(1, l22))), 'l2': ListNode(3, l22)}
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        print(s.getIntersectionNode(test_case['l1'], test_case['l2']).val)

    print('Solution2')
    s = Solution2()
    for test_case in test_cases:
        print(s.getIntersectionNode(test_case['l1'], test_case['l2']).val)


if __name__ == '__main__':
    main()
