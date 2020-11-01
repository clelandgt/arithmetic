# -*- coding: utf-8 -*-
# @File  : sort_list.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-01
# @Desc  :


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_link(head: ListNode) -> ListNode:
    p = head
    while p:
        if p.next:
            print(p.val, end='->')
        else:
            print(p.val)
        p = p.next
    print('\n')


class Solution1:
    """归并排序(递归)
    时间复杂度: O(nlogn)
    空间复杂度: O(1)
    """
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # mid
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid, slow.next = slow.next, None

        # 合并
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode):
        # left = 2, 7, 9   right = 3, 5, 8
        # p = 2, 3, 5, 7, 8, 9
        if not left or not right:
            return left or right

        head = p = ListNode(0)
        while left and right:
            if left.val <= right.val:
                p.next, left = left, left.next
            else:
                p.next, right = right, right.next
            p = p.next
        p.next = left or right

        return head.next


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        pass


def main():
    # 4->2->1->3
    # -1->5->3->4->0
    test_cases = [
        ListNode(4, ListNode(2, ListNode(1, ListNode(3)))),
        ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        result = s1.sortList(test_case)
        print_link(result)

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        result = s2.sortList(test_case)
        print_link(result)


if __name__ == '__main__':
    main()
