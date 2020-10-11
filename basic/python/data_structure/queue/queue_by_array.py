# -*- coding: utf-8 -*-
# @File  : queue_by_array.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  :


class ArrayQueue:
    def __init__(self, capacity):
        self.__head = 0
        self.__tail = 0
        self.__queue = [None] * capacity
        self.__capacity = capacity

    def enqueue(self, item):
        # 当插入的index大于capacity，对数组进行一次清洗，清洗出前面空余的index.
        if self.__tail == self.__capacity:
            if self.__head == 0:
                raise Exception('队列已满')
            else:
                for i in range(self.__tail-self.__head):
                    self.__queue[i] = self.__queue[self.__head+i]
                self.__tail = self.__tail - self.__head
                self.__head = 0

        # 入队
        self.__queue.insert(self.__tail, item)
        self.__tail += 1

    def dequeue(self):
        if self.__head != self.__tail:
            item = self.__queue[self.__head]
            self.__head += 1
            return item

    def __repr__(self):
        for i in range(self.__head+1, self.__tail)[::-1]:
            print(self.__queue[i], end='-->')
        print(self.__queue[self.__head])


def main():
    que = ArrayQueue(10)
    for i in range(8):
        que.enqueue(i)
    que.__repr__()
    for _ in range(5):
        que.dequeue()
    que.__repr__()
    for i in range(4):
        que.enqueue(i)
    que.__repr__()


if __name__ == '__main__':
    main()
