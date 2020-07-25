# -*- coding: utf-8 -*-
# @File  : daily_temperatures.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-24
# @Desc  :
from typing import List


class Solution1:
    """暴力破解 超时"""
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = []
        for i in range(len(T)):
            index = 1
            find = False
            for j in range(i+1, len(T)):
                if T[i] >= T[j]:
                    index += 1
                else:
                    find = True
                    break
            if find:
                result.append(index)
            else:
                result.append(0)

        return result


class Solution2:
    """暴力破解: 代码更加优雅"""
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        for i in range(len(T)):
            for j in range(i, len(T)):
                if T[j] > T[i]:
                    res[i] = j - i
                    break #guarentee the soonest
        return res


class Solution3:
    """使用栈"""
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while(stack and T[i] >= T[stack[-1]]):
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


def main():
    test_cases = [
        [73, 74, 75, 71, 69, 72, 76, 73]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.dailyTemperatures(test_case))

    print('Solution2')
    s1 = Solution2()
    for test_case in test_cases:
        print(s1.dailyTemperatures(test_case))


if __name__ == '__main__':
    main()
