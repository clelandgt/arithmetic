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
            # 有上升趋势
            if flag == 0:
                if A[i] < A[i+1]:
                    flag = 1
                else:
                    return False
            # 达到顶点
            elif flag == 1:
                if A[i] > A[i + 1]:
                    flag = 2
                else:
                    pass
            elif flag == 2:
                if A[i] > A[i + 1]:
                    pass
                else:
                    return False
        if flag == 2:
            return True
        else:
            return False


def main():
    test_cases = [
        [[2, 1], False],
        [[1, 3, 2], True],
        [[3, 5, 5], False],
        [[0, 3, 2, 1], True],
        [[14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3], True]
    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.validMountainArray(test_case[0]))



if __name__ == '__main__':
    main()

