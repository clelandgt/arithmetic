# -*- coding: utf-8 -*-
# @File  : bucket_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 桶排序. 参考：https://github.com/TheAlgorithms/Python/blob/master/sorts/bucket_sort.py

BUCKET_SIZE = 5


def bucket_sort(nums, bucket_size=BUCKET_SIZE):
    min_value, max_value = min(nums), max(nums)

    # 分桶
    bucket_count = ((max_value - min_value) // BUCKET_SIZE) + 1
    buckets = [[] for _ in range(bucket_count)]

    for i in range(len(nums)):
        buckets[(nums[i] - min_value) // bucket_size].append(nums[i])

    # 桶内排序
    return sorted(
        [buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))]
    )


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]
    for test_case in test_cases:
        print('before sort:', test_case)
        print('after sort:', bucket_sort(test_case))


if __name__ == '__main__':
    main()
