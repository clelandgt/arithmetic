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


def print_link(l: ListNode):
    while l:
        if l.next is not None:
            print(f'{l.val}', end='->')
        else:
            print(f'{l.val}', end='')
        l = l.next
    print('\n')


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


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 头指针
        head = ListNode(0)
        p = head
        carry = 0
        while l1 or l2:
            total = 0
            # l1与l2都非空
            if l1 and l2:
                total = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                total = l1.val + carry
                l1 = l1.next
            elif not l1 and l2:
                total = l2.val + carry
                l2 = l2.next

            p.next = ListNode(total % 10)
            carry = total // 10
            p = p.next

        # 最高位是否有进位
        if carry == 1:
            p.next = ListNode(carry)

        return head.next


def main():
    # l1: 2->4->3->1
    # l2: 1->8->5
    l1 = ListNode(2, ListNode(4, ListNode(3, ListNode(1))))
    l2 = ListNode(1, ListNode(8, ListNode(5)))
    s = Solution1()
    links = s.addTwoNumbers(l1, l2)
    print('Solution1: ')
    print_link(links)

    s = Solution2()
    links = s.addTwoNumbers(l1, l2)
    print('Solution2: ')
    print_link(links)


if __name__ == '__main__':
    main()

