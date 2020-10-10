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
    def __init__(self, value=None):
        if value is not None:
            self.__head = Node(value)
        else:
            self.__head = None

    def get_head(self):
        return self.__head

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

    def insert_node_to_head(self, node):
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

    def insert_node_to_tail(self, node):
        if self.__head is None:
            self.insert_node_to_head(node)
            return

        p = self.__head
        while p.node_next is not None:
            p = p.node_next
        p.node_next = node

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
        p = self.__head
        if p is None:
            return
        pre, cur, next = None, p, p.node_next
        while cur:
            cur.node_next = pre
            pre = cur
            cur = next
            if next is None:
                next = None
            else:
                next = next.node_next
        self.__head = pre

    def has_ring(self):
        """是否成环"""
        head = self.__head
        if head is None or head.node_next is None:
            return False

        slow, fast = head, head.node_next.node_next
        while fast is not None:
            if slow == fast:
                return True
            slow = slow.node_next
            if fast.node_next:
                fast = fast.node_next.node_next
            else:
                return False

        return False


def main():
    sl = SingleLinkedList()
    for i in range(10):
        sl.insert_to_tail(i)
    sl.print_all()

    sl.delete_by_value(6)
    sl.print_all()

    # 查找元素
    print('------ 查找元素 ------')
    node1 = sl.find_by_value(4)
    if node1:
        print(node1.data)

    node2 = sl.find_by_value(4)
    if node2:
        print(node2.data)

    # 数组反转
    print('------ 数组反转 ------')
    sl.reversed_self()
    sl.print_all()

    # 判断是否成环
    # head = [3, 2, 0, -4] pos = 1
    print('------ 判断是否成环 ------')
    sl2 = SingleLinkedList()
    sl2.insert_to_tail(3)
    node1 = Node(2)
    sl2.insert_node_to_tail(node1)
    sl2.insert_to_tail(0)
    node2 = Node(-4)
    node2.node_next = node1
    sl2.insert_node_to_tail(node2)
    print(sl2.has_ring())
    print(sl.has_ring())
    print(SingleLinkedList().has_ring())
    print(SingleLinkedList(1).has_ring())


if __name__ == '__main__':
    main()
