# -*- coding: utf-8 -*-
# @File  : queue_by_linked.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  :


class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self, item):
        if self.__tail is None:
            self.__head = ListNode(item)
            self.__tail = self.__head
        else:
            self.__tail.next = ListNode(item)
            self.__tail = self.__tail.next

    def dequeue(self):
        if self.__head:
            val = self.__head.val
            self.__head = self.__head.next
            return val

    def __repr__(self):
        values = []
        p = self.__head
        while p:
            values.append(p.val)
            p = p.next
        values = values[::-1]
        return '->'.join(str(value) for value in values)


def main():
    lq = LinkedQueue()
    for i in range(10):
        lq.enqueue(i)
    print(lq.__repr__())

    for _ in range(4):
        lq.dequeue()
    print(lq.__repr__())

    for i in range(100):
        lq.enqueue(i)
    print(lq.__repr__())


if __name__ == '__main__':
    main()
