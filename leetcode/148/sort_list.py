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

    def print_link(self, head: ListNode) -> ListNode:
        p = head
        while p:
            if p.next:
                print(p.val, end='->')
            else:
                print(p.val)
            p = p.next
        print('\n')


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
        s1.print_link(result)


if __name__ == '__main__':
    main()
