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
        new_array = DynamicArray(new_capacity)
        for i in range(self.__size):
            new_array.add(new_array.__size, self.__data[i])
        self.__capacity = new_capacity
        self.__data = new_array.__data

    def add(self, index, item):
        if index < 0 or index > self.__size:
            raise Exception('Add failed, index must between 0~_{}'.format(self.__size))

        if self.__size != 0 and self.__size % self.__capacity == 0:
            self._resize(self.__capacity * 2)

        if index == self.__size:
            self.__data[index] = item
        else:
            for i in range(index, self.__size)[::-1]:
                self.__data[i+1] = self.__data[i]
            self.__data[index] = item
        self.__size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise Exception('Get failed. Index is illegal.')
        return self.__data[index]

    def set(self, index, item):
        if index < 0 or index >= self._size:
            raise Exception('Get failed. Index is illegal.')
        self.__data[index] = item

    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise Exception('Remove failed. Index is illegal.')
        for i in range(index, self.__size):
            self.__data[i] = self.__data[i+1]
        self.__size -= 1
        self.__data[self.__size] = None

        if self.__size and self.__capacity // self.__size == 4:
            self._resize(self.__capacity // 2)

    def get_capacity(self):
        return self.__capacity

    def print_array(self):
        print(self.__data)


def main():
    da = DynamicArray(5)
    for i in range(50):
        da.add(i, i+2)
    print('capacity: ', da.get_capacity())
    da.print_array()

    for _ in range(30):
        da.remove(1)
    print('capacity: ', da.get_capacity())
    da.print_array()


if __name__ == '__main__':
    main()
