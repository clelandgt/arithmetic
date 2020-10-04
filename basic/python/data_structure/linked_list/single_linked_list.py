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
        node = Node(value)
        node.node_next = self.__head
        self.__head = node

    def insert_after(self, node, value):
        if node is None:
            return

        new_node = Node(value)
        new_node.node_next = node.node_next
        node.node_next = new_node

    def insert_before(self, node, value):
        if (node is None) or (self.__head is None):
            return

        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        p = self.__head

        not_found = False
        while p.next_node != node:
            if p.next_node is None:
                not_found = True
                break
            else:
                p = p.next_node
        if not not_found:
            p.next_node = new_node
            new_node.node_next = node

    def insert_to_tail(self, value):
        if self.__head is None:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        p = self.__head
        while p is not None:
            p = p.next_node
        p.next_node = new_node

    def print_all(self):
        p = self.__head
        if p is None:
            print("当前链表没有数据")

        while p.next is None:
            print(str(p.data) + " --> ", end="")
            p = p.next_node
        print(str(p.value))

    def reversed_self(self):
        pass

    def has_ring(self):
        pass


def main():
    sl = SingleLinkedList()
    for i in range(10):
        sl.insert_to_tail(i)
    sl.print_all()



if __name__ == '__main__':
    main()
