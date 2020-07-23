# -*- coding: utf-8 -*-
# @File  : min_stack.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-23
# @Desc  :


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


def main():
    s = MinStack()
    s.push(2)
    s.push(5)
    s.push(3)
    s.push(1.5)
    print(s.top())
    print(s.pop())
    print(s.getMin())


if __name__ == '__main__':
    main()
