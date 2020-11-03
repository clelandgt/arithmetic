# -*- coding: utf-8 -*-
# @File  : valid_mountain_array.py
# @Author: clelandgt@163.com
# @Date  : 2020-11-03
# @Desc  :
from typing import List


class Solution1:
    """ 使用状态流转来描述山脉
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        flag = 0

        for i in range(len(A)-1):
            # 递增
            if flag == 0:
                if A[i] < A[i+1]:
                    flag = 1
                else:
                    return False
            # 达到顶点
            elif flag == 1:
                if A[i] > A[i + 1]:
                    flag = 2
            # 递减
            elif flag == 2:
                if A[i] <= A[i + 1]:
                    return False

        if flag == 2:
            return True
        else:
            return False


class Solution2:
    """ 双指针遍历
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def validMountainArray(self, A: List[int]) -> bool:
        size = len(A)
        if size < 3:
            return False
        left, right = 0, size - 1
        while left <= size-2 and A[left] < A[left+1]:
            left += 1
        while right-1 >= 0 and A[right-1] > A[right]:
            right -= 1
        return left == right and right < size-1 and left > 0


def main():
    test_cases = [
        [[2, 1], False],
        [[1, 3, 2], True],
        [[3, 5, 5], False],
        [[0, 3, 2, 1], True],
        [[14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3], True],
        [[0,1,2,3,4,5,6,7,8,9], False],
        [[9,8,7,6,5,4,3,2,1,0], False]


    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.validMountainArray(test_case[0]))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.validMountainArray(test_case[0]))


if __name__ == '__main__':
    main()

