# -*- coding: utf-8 -*-
# @File  : get_min_distance_pointers.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-11
# @Desc  :

"""
问题描述: 二维平面上有 n 个点，如何快速计算出两个距离最近的点对
参考：
1. https://blog.csdn.net/lonelycatcher/article/details/7973046
2. https://blog.csdn.net/sinat_35678407/article/details/82874216?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase
"""
import numpy as np


def timeit(method):
    import time

    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()
        spend_time = int((end_time - start_time) * 1000)
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = spend_time
        else:
            print('{0}: {1} ms'.format(method.__name__, spend_time))

        return result
    return timed


def get_distance(pointer1, pointer2):
    return ((pointer1[0]-pointer2[0]) ** 2 + (pointer1[1]-pointer2[1]) ** 2) ** 0.5


@timeit
def get_min_distance_pointers1(pointers):
    """ 暴力求解: O(n^2), 依次遍历两两比较 """
    pointer1 = None
    pointer2 = None
    min_distance = float('inf')
    for i in range(len(pointers)):
        for j in range(i+1, len(pointers)):
            distance = get_distance(pointers[i], pointers[j])
            if distance <= min_distance:
                min_distance = distance
                pointer1 = pointers[i]
                pointer2 = pointers[j]
    return pointer1, pointer2, min_distance


@timeit
def get_min_distance_pointers2(pointers):
    return _get_min_distance_pointers2(pointers)


def _get_min_distance_pointers2(pointers):
    """ 分治解决 """
    nums = len(pointers)
    mid = int(nums / 2)
    if nums < 2:
        return None, None, 0
    elif nums == 2:
        return pointers[0], pointers[1], get_distance(pointers[0], pointers[1])
    elif nums == 3:
        distance1 = get_distance(pointers[0], pointers[1])
        distance2 = get_distance(pointers[0], pointers[2])
        distance3 = get_distance(pointers[1], pointers[2])
        if distance1 < distance2 and distance1 < distance3:
            return pointers[0], pointers[1], distance1
        if distance2 < distance1 and distance2 < distance3:
            return pointers[0], pointers[2], distance2
        if distance3 < distance1 and distance3 < distance2:
            return pointers[1], pointers[2], distance3

    left_pointers1, left_pointers2, left_distance = _get_min_distance_pointers2(pointers[:mid])
    right_pointers1, right_pointers2, right_distance = _get_min_distance_pointers2(pointers[mid:])

    # 单边的最小值
    if left_distance <= right_distance:
        min_distance = left_distance
        min_pointers1 = left_pointers1
        min_pointers2 = left_pointers2
    else:
        min_distance = right_distance
        min_pointers1 = right_pointers1
        min_pointers2 = right_pointers2

    # x轴筛选出 (mid-min_distance, mid+min_distance)
    x_pointers = [item for item in pointers if item[0] >= (pointers[mid][0] - min_distance) and item[0] <= (pointers[mid][0] + min_distance)]
    # 筛选后的数组，按照y值进行排序
    x_pointers = sorted(x_pointers, key=lambda x: x[1])
    # d*2d范围内查找最小值
    for i in range(len((x_pointers))):
        base_pointers = x_pointers[i]
        for j in range(i+1, len((x_pointers))):
            if (x_pointers[j][1] - base_pointers[1]) > min_distance:
                break
            distance = get_distance(base_pointers, x_pointers[j])
            if distance < min_distance:
                min_distance = distance
                min_pointers1 = base_pointers
                min_pointers2 = x_pointers[j]
    return min_pointers1, min_pointers2, min_distance


def main():
    test_cases = [
        [],
        [[1, 1]],
        [[1, 1], [9, 3]],
        [[1, 1], [9, 3], [4, 5]],
        [[1, 1], [9, 3], [4, 5], [-1, -2]],
        np.random.randint(1, 100000, 5000).reshape(2500, 2).tolist()
    ]

    print('法一: 暴力求解')
    for index, item in  enumerate(test_cases):
        print(f'case {index}: {get_min_distance_pointers1(item)}')

    print('\\n')
    print('法二: 分治')
    for index, item in  enumerate(test_cases):
        item = sorted(item, key=lambda x: x[0])
        print(f'case {index}: {get_min_distance_pointers2(item)}')


if __name__ == '__main__':
    main()
