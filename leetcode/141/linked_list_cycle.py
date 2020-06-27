# -*- coding: utf-8 -*-
# @File  : linked_list_cycle.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-28
# @Desc  :


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def hasCycle(self, head: ListNode) -> bool:
        result = set()

        p = head
        while p:
            if id(p) in result:
                return True
            result.add(id(p))
            p = p.next
        return False


def main():
    # case1: [3,2,0,-4], pos = 1
    # case2: head = [1, 2], pos = 0
    # case3: head = [1], pos = -1
    head1 = ListNode(3)
    p1 = head1
    p1.next = ListNode(2)
    p1 = p1.next
    p1.next = ListNode(0)
    p1 = p1.next
    p1.next = ListNode(-4)
    p1 = p1.next
    p1.next = head1.next

    head2 = ListNode(1)
    p2 = head2
    p2.next = ListNode(2)
    p2 = p2.next
    p2.next = head2

    test_cases = [
        head1,
        head2,
        ListNode(1)
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        print(s.hasCycle(test_case))


if __name__ == '__main__':
    main()


