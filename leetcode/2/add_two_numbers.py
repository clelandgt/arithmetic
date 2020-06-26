# -*- coding: utf-8 -*-
# @File  : add_two_numbers.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-26
# @Desc  :


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        时间复杂度 O(n), 空间复杂度 O(n)
        :param l1:
        :param l2:
        :return:
        """
        result = ListNode(0, None)
        current_node = result
        while l1 or l2:
            x1 = l1.val if l1 is not None else 0
            x2 = l2.val if l2 is not None else 0

            total = current_node.val + (x1 + x2)
            current_node.val = total % 10
            current_node.next = ListNode(int(total/10), None)
            current_node = current_node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # 当最后节点为0时，剔除。
        link = result
        while link.next is not None:
            if link.next.next is None and link.next.val == 0:
                link.next = None
                break
            link = link.next

        return result

    @staticmethod
    def print_link(l: ListNode):
        while l:
            if l.next is not None:
                print(f'{l.val}', end='->')
            else:
                print(f'{l.val}', end='')
            l = l.next


def main():
    # l1: 2->4->3->1
    # l2: 1->8->5
    l1 = ListNode(2, ListNode(4, ListNode(3, ListNode(1))))
    l2 = ListNode(1, ListNode(8, ListNode(5)))
    s = Solution1()
    links = s.addTwoNumbers(l1, l2)
    s.print_link(links)


if __name__ == '__main__':
    main()

