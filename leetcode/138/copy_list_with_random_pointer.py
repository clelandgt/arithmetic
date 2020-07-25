# -*- coding: utf-8 -*-
# @File  : copy_list_with_random_pointer.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-25
# @Desc  :
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        mapping = {}
        p = head
        while p:
            mapping[p] = Node(p.val, None, None)
            p = p.next

        p = head
        while p:
            if p.next:
                mapping[p].next = mapping[p.next]
            if p.random:
                mapping[p].random = mapping[p.random]
            p = p.next

        return mapping[head]


def main():
    print('Solution1')


if __name__ == '__main__':
    main()
