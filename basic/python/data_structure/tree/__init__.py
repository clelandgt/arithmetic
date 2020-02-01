# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Cleland
# @Date  : 2019-03-01
# @Desc  : 当前都是基于链表实现
from abc import abstractmethod


class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree(Node):
    def __init__(self):
        super(__class__, self).__init__()

    @abstractmethod
    def insert(self, value):
        """ 插入
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def find(self, value):
        """ 查找
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def delete(self, value):
        """ 删除
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def get_max(self, value):
        """ 获取最大值
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def get_min(self, value):
        """ 获取最小值
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def pre_order(self):
        """ 前序遍历
        :return:
        """
        pass

    @abstractmethod
    def in_order(self):
        """ 中序遍历
        :return:
        """
        pass

    @abstractmethod
    def post_order(self):
        """ 后序遍历
        :return:
        """
        pass

    @abstractmethod
    def bfs(self):
        """ 广度优先遍历(借助队列)

        :return:
        """
        # TODO: 待补充
        raise NotImplementedError

    @abstractmethod
    def dfs(self):
        """ 深度优先遍历(借助栈)

        :return:
        """
        # TODO: 待补充
