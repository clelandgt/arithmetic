# -*- coding: utf-8 -*-
# @File  : linked_list_cycle.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-28
# @Desc  : 判断是否成环


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """ 哈希表
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def hasCycle(self, head: ListNode) -> bool:
        result = set()

        while head:
            if id(head) in result:
                return True
            result.add(id(head))
            head = head.next
        return False


class Solution2:
    """ 修改遍历过的节点. 注意点: 会修改原链表的值
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val == 10**6:
                return True
            head.val = 10**6
            head = head.next
        return False


class Solution3:
    """ 双指针，快慢指针
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

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
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.hasCycle(test_case))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.hasCycle(test_case))

    print('Solution3')
    s3 = Solution3()
    for test_case in test_cases:
        print(s3.hasCycle(test_case))


if __name__ == '__main__':
    main()


