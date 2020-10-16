# -*- coding: utf-8 -*-
# @File  : 0_1_bag.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-15
# @Desc  :

max_size = float('-inf')


def _bag(i, nums, current_size, bag_size):
    global max_size

    if current_size == bag_size or i == len(nums):
        if current_size > max_size:
            max_size = current_size
        return

    # 当前物品不放入背包
    _bag(i+1, nums, current_size, bag_size)
    # 当前物品放入背包
    if current_size + nums[i] <= bag_size:
        _bag(i+1, nums, current_size+nums[i], bag_size)


def bag(nums, bag_size):
    _bag(0, nums, 0, bag_size)
    return max_size


def main():
    test_cases = [
        ([3, 1, 2, 5, 1, 3, 4, 8], 7)
    ]
    for test_case in test_cases:
        print(bag(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
