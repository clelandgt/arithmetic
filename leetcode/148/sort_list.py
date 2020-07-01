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
    def sortList(self, head: ListNode) -> ListNode:
        """选择排序
        leetcode 上超时了....
        """
        p = head
        while p and p.next:
            min_node = p
            p11 = p.next
            while p11:
                if p11.val < min_node.val:
                    min_node = p11
                p11 = p11.next
            if p.val != min_node.val:
                p.val, min_node.val = min_node.val, p.val
            p = p.next

        return head


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        """
        """
        if not head or not head.next:
            return head

        # mid
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(second)
        return self.merge(left, right)

    # l = 2, 7, 9   r = 3, 5, 8
    # m = 2, 3, 5,
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        if not left or not right:
            return left or right
        # 找到以left, right为起点
        if left.val > right.val:
            right, left = left, right
        head = pre = left
        left = left.next

        while left and right:
            if left.val < right.val:
                left = left.next
            else:
                next = pre.next
                pre.next = right
                tmp = right.next
                right.next = next
                right = tmp

            pre = pre.next
        pre.next = left or right
        return head


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
