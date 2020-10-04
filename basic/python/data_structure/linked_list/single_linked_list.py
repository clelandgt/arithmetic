# -*- coding: utf-8 -*-
# @File  : single_linked_list.py
# @Author: tao.gan@advance.ai
# @Date  : 2020-10-04
# @Desc  :


class Node(object):
    """链表节点"""
    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def data(self):
        return self.__value

    @data.setter
    def data(self, value):
        self.__value = value

    @property
    def node_next(self):
        return self.__next

    @ node_next.setter
    def node_next(self, next):
        self.__next = next


class SingleLinkedList(object):
    def __init__(self):
        self.__head = None

    def delete_by_node(self, node):
        pass

    def delete_by_value(self, value):
        pass

    def find_by_value(self, value):
        pass

    def find_by_index(self, index):
        pass

    def insert_to_head(self, value):
        pass

    def insert_after(self, node, value):
        pass

    def insert_before(self, node, value):
        pass

    def print_all(self):
        pass

    def reversed_self(self):
        pass

    def has_ring(self):
        pass


def main():
    sl = SingleLinkedList()


if __name__ == '__main__':
    main()
