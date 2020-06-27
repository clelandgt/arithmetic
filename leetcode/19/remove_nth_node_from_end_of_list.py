# -*- coding: utf-8 -*-
# @File  : remove_nth_node_from_end_of_list.py
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        length = 0
        # 计算链表的长度
        while p:
            length += 1
            p = p.next

        del_index = length - n
        if del_index < 0:
            return head

        # 定位需要删除的节点
        if del_index == 0:
            return head.next

        index = 0
        p = head
        while p:
            if index == del_index - 1:
                next_node = p.next
                p.next = next_node.next
                del next_node
                return head
            index += 1
            p = p.next


def main():
    # list 1->2->3->4->5  n = 2
    test_cases = [
        {'list': ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 'n': 2},
        {'list': ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 'n': 1}
    ]

    print('Solution1')
    s = Solution1()
    for test_case in test_cases:
        tmp_link = s.removeNthFromEnd(test_case['list'], test_case['n'])
        print_link(tmp_link)


if __name__ == '__main__':
    main()
