# -*- coding: utf-8 -*-
# @File  : dynamic_array.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-26
# @Desc  : 实现一个支持动态扩容的数组, 并完成增删改差. 参考: https://blog.csdn.net/u013109501/article/details/88020739


class DynamicArray(object):
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size = 0
        self.__data = [None] * capacity

    def _resize(self, new_capacity):
        pass

    def add(self, index, item):
        if index < 0 or index > self.__size:
            raise Exception('Add failed, index must between 0~_{}'.format(self.__size))

        if index == self.__size:
            self.__data[index] = item
        else:
            for i in range(index, self.__size)[::-1]:
                self.__data[i+1] = self.__data[i]
            self.__data[index] = item
        self.__size += 1

        if self.__size % self.__capacity == 0:
            self._resize(self.__capacity * 2)

    def get(self, index):
        pass

    def set(self, index, item):
        pass

    def remove(self, index):
        pass

    def print_array(self):
        for item in self.__data:
            print(item)


def main():
    da = DynamicArray(5)
    for i in range(50):
        da.add(i, i+2)
    da.print_array()


if __name__ == '__main__':
    main()
