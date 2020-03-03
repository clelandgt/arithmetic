# -*- coding: utf-8 -*-
# @File  : counting_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 计数排序  https://time.geekbang.org/column/article/42038


def counting_sort(nums):
    max_value = max(nums)
    frequencies = [0 for _ in range(max_value+1)]

    # 统计每个数出现的频数，放到frequencies
    for num in nums:
        frequencies[num] += 1

    # 一次累加
    for i in range(len(frequencies)-1):
        frequencies[i+1] = frequencies[i] + frequencies[i+1]

    # 定义 results, 存储排序后的数组
    results = [None for _ in nums]
    for num in nums:
        index = frequencies[num]-1
        results[index] = num
        frequencies[num] -= 1

    return results


def main():
    nums = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print('before sort:', nums)
    nums = counting_sort(nums)
    print('after sort:', nums)


if __name__ == '__main__':
    main()
