# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Cleland
# @Date  : 2019-03-01
# @Desc  :
from abc import abstractmethod


class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree(object):
    def __init__(self):
        pass

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
