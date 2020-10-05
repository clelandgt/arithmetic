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
        p = self.__head
        while p.node_next:
            if p.node_next == node:
                p.node_next = node.node_next
            else:
                p = p.node_next

    def delete_by_value(self, value):
        p = self.__head
        if p is None:
            raise Exception('value not found')
        while p.node_next:
            if p.node_next.data == value:
                p.node_next = p.node_next.node_next
                return
            p = p.node_next
        raise Exception('value not found')

    def find_by_value(self, value):
        p = self.__head
        if p is None:
            raise Exception('value not found')
        while p:
            if p.data == value:
                return p
            else:
                p = p.node_next

    def find_by_index(self, index):
        p = self.__head
        position = 0
        if p is None:
            raise Exception('value not found')
        while p:
            if position == index:
                return p
            else:
                p = p.node_next
                position += 1

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
        while p.node_next != node:
            if p.node_next is None:
                not_found = True
                break
            else:
                p = p.node_next
        if not not_found:
            p.node_next = new_node
            new_node.node_next = node

    def insert_to_tail(self, value):
        if self.__head is None:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        p = self.__head
        while p.node_next is not None:
            p = p.node_next
        p.node_next = new_node

    def print_all(self):
        p = self.__head
        if p is None:
            print("当前链表没有数据")

        while p.node_next is not None:
            print(str(p.data) + " --> ", end="")
            p = p.node_next
        print(str(p.data))

    def reversed_self(self):
        """链表反转"""
        pass

    def has_ring(self):
        """是否成环"""
        pass


def main():
    sl = SingleLinkedList()
    for i in range(10):
        sl.insert_to_tail(i)
    sl.print_all()

    sl.delete_by_value(6)
    sl.print_all()

    node1 = sl.find_by_value(4)
    if node1:
        print(node1.data)

    node2 = sl.find_by_value(4)
    if node2:
        print(node2.data)


if __name__ == '__main__':
    main()
