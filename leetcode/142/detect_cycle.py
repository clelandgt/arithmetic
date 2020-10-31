# -*- coding: utf-8 -*-
# @File  : detect_cycle.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-31
# @Desc  : 环形链表，入环的位置
# 解法：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/142-huan-xing-lian-biao-ii-jian-hua-gong-shi-jia-2/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """双指针 快慢指针
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        # 相遇
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return

        # 入环位置
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast


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
    s1 = Solution1()
    for test_case in test_cases:
        node = s1.detectCycle(test_case)
        if node:
            print(s1.detectCycle(test_case).val)
        else:
            print('null')


if __name__ == '__main__':
    main()
