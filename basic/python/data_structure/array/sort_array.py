# -*- coding: utf-8 -*-
# @File  : sort_array.py
# @Author: tao.gan@advance.ai
# @Date  : 2020-10-04
# @Desc  : https://blog.csdn.net/weixin_43633501/article/details/90110507


class SortArray(object):
    def __init__(self, capacity=10):
        self.__size = 0
        self.__capacity = capacity
        self.__data = [None] * capacity

    def add(self, item):
        if self.__size == 0:
            self.__data[0] = item
            self.__size += 1
            return
        if self.__size == self.__capacity:
            raise Exception("数组已满")

        # 倒序遍历向后移动数组，直到元素插入
        is_find = False
        for i in range(self.__size)[::-1]:
            if item < self.__data[i]:
                self.__data[i+1] = self.__data[i]
            else:
                is_find = True
                break
        if is_find is True:
            self.__data[i+1] = item
        else:
            self.__data[i] = item
        self.__size += 1

    def remove(self, item):
        pass

    def print_array(self):
        print(self.__data)


def main():
    sa = SortArray(100)
    for i in range(20):
        sa.add(i*2)
    sa.add(11)
    sa.add(-2)
    sa.print_array()


if __name__ == '__main__':
    main()
