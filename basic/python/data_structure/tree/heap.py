# -*- coding: utf-8 -*-
# @File  : heap.py
# @Author: Cleland
# @Date  : 2019-03-02
# @Desc  : 基于数组是实现，堆与堆排序: 1.建堆；2.往堆中插入一个元素；3.删除堆顶元素；4.堆排序
#          这里都是基于大顶堆实现。


class Heap(object):
    def __init__(self):
        """ 结构化

        """
        self.data = [0]
        self.count = 0

    def build_heap(self, nums):
        """ 堆化

        :param nums:
        :return:
        """
        self.data = [0]
        self.count = len(nums)
        for num in nums:
            self.data.append(num)

        n = self.count
        for i in range(1, (n/2)+1)[::-1]:
            self.heapify(self.data, n, i)

    def insert(self, value):
        """ 堆中插入一个元素
        插入的数据与父节点进行比较，如果比父节点大，交换数据。

        :param value:
        :return:
        """
        items = self.data
        items.append(value)
        self.count += 1

        # 堆为空
        if self.count == 1:
            return

        n = self.count
        while n > 0:
            parent_index = n / 2
            if items[n] > items[parent_index]:
                items[n], items[parent_index] = items[parent_index], items[n]
                n = parent_index
            else:
                break

    def delete_top(self):
        """ 删除堆顶元素
        将最右子叶子替换顶元素(只做数据交换，数组就不会出现空洞)，再从上往下进行堆化。

        :return:
        """
        self.count -= 1

        if self.count == 0:
            self.data.pop(self.count+1)
            return

        self.data[1] = self.data.pop()

        # 堆化
        self.heapify(self.data, self.count, 1)

    @staticmethod
    def heapify(nums, n, i):
        """ 堆化
        逐一比较两个子节点，如果存在比子节点小且，找到最大的一个子节点进行置换。
        :param nums: 数组构成的堆
        :param n: 堆的大小
        :param i: 第i个元素
        :return:
        """
        while True:
            max_pos = i
            if i*2 <= n and nums[i] < nums[i*2]:
                max_pos = i * 2
            if i*2+1 <= n and nums[max_pos] < nums[i*2+1]:
                max_pos = i * 2 + 1
            if max_pos == i:
                break
            nums[i], nums[max_pos] = nums[max_pos], nums[i]
            i = max_pos

    def sort(self, nums=[]):
        """ 堆排序
        步骤:
        1. 堆化
        2. 排序

        :return:
        """
        if len(nums) != 0:
            self.build_heap(nums)
        if self.count < 1:
            return
        for i in range(2, self.count+1)[::-1]:
            self.data[1], self.data[i] = self.data[i], self.data[1]
            self.heapify(self.data, i-1, 1)


def test():
    """ 测试
    1. 测试堆的插入与删除
    2. 测试堆排序
    :return:
    """
    # 堆的插入与删除
    """
                33
              /     \
            27       21
           / \      / \
         16   13   15  9
         /\   /\   /\
        5  6 7  8  1 2
    """

    heap = Heap()
    heap.build_heap([33, 27, 21, 16, 13, 15, 9, 5, 6, 7, 8, 1, 2])
    print '初始化堆: ', heap.data

    heap.insert(22)
    print u'堆插入后: ', heap.data

    heap.delete_top()
    print u'堆插删除头元素: ', heap.data

    # 堆排序测试
    heap = Heap()
    heap.build_heap([2, 8, 10, 1, 3, 7, 5, 6, 9, 20, 15])
    print u'堆化的元素: ', heap.data
    heap.sort()
    print u'堆排序后的元素: ', heap.data
