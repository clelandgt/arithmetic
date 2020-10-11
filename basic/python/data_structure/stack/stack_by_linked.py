# -*- coding: utf-8 -*-
# @File  : stack_by_linked.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  : head在栈顶


class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Stack:
    def __init__(self):
        self.__stack = None

    def top(self):
        return None if self.is_empty() else self.__stack.val

    def push(self, value):
        node = ListNode(value)
        node.next = self.__stack
        self.__stack = node

    def pop(self):
        if self.is_empty() is not None:
            val = self.__stack.val
            self.__stack = self.__stack.next
            return val

    def clear(self):
        self.__stack = ListNode()

    def is_empty(self):
        if self.__stack is None:
            return True
        return False

    def length(self):
        p = self.__stack
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def __str__(self):
        result = ''
        p = self.__stack
        if p is None:
            return ''

        while p.next is not None:
            result += f'{p.val} -->'
            p = p.next

        result += f'{p.val}'
        return result


def main():
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print('length: ', stack.length())
    print('push: ', str(stack))

    print('top: ', stack.top())
    for _ in range(2):
        stack.pop()
    print('pop: ',  str(stack))
    str(stack)
    stack.clear()
    print('clear: ',  str(stack))
    str(stack)
    print('is_empty: ', stack.is_empty())


if __name__ == '__main__':
    main()
