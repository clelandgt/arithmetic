# -*- coding: utf-8 -*-
# @File  : stack_by_array.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  :


class Stack:
    def __init__(self):
        self.__stack = []

    def top(self):
        return None if self.is_empty() else self.__stack[-1]

    def push(self, value):
        return self.__stack.append(value)

    def pop(self):
        return None if self.is_empty() else self.__stack.pop()

    def clear(self):
        self.__stack = []

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        return False

    def length(self):
        return len(self.__stack)

    def __str__(self):
        return str(self.__stack)


def main():
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print('length: ', stack.length())
    print('push: ', str(stack))
    print('top: ', stack.top())
    for _ in range(2):
        stack.pop()
    print('pop: ', str(stack))
    stack.clear()
    print('clear: ', str(stack))
    print('is_empty: ', stack.is_empty())


if __name__ == '__main__':
    main()
