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
    @staticmethod
    def reversed_link(l):
        """ 反转链表函数
            2->4->3->1
        =>  2<-4<-3<-1
        :param l:
        :return:
        """
        result = None
        last_node = None
        while l is not None:
            result = ListNode(l.val, last_node)
            last_node = result
            l = l.next

        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 反转链表
        l11 = self.reversed_link(l1)
        l22 = self.reversed_link(l2)

        # ADD
        result = ListNode(0, None)
        current_node = result
        while True:
            x1, x2 = 0, 0
            if l11 is not None:
               x1 = l11.val
            if l22 is not None:
               x2 = l22.val

            total = current_node.val + x1 + x2
            current_node.val = total % 10
            if l11 is not None:
                l11 = l11.next
            if l22 is not None:
                l22 = l22.next

            if l11 is None and l22 is None:
                break
            current_node.next = ListNode(int(total/10), None)
            current_node = current_node.next

        # return 结果
        return result

    @staticmethod
    def print_link(l: ListNode):
        while l:
            print(f'{l.val}', end='->')
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

