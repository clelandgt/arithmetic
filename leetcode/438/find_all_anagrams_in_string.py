# -*- coding: utf-8 -*-
# @File  : find_all_anagrams_in_string.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-25
# @Desc  :
from typing import List
from collections import Counter


class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return res
        counter_p = Counter(p)
        for i in range(len(s)-len(p)+1):
            if Counter(s[i:i+len(p)]) == counter_p:
                res.append(i)

        return res


class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, s_len, p_len = [], len(s), len(p)
        if p_len > s_len:
            return []
        hash_p, hash_s = 0, 0
        for i in range(p_len):
            hash_p += hash(p[i])
            hash_s += hash(s[i])
        if hash_p == hash_s:
            res.append(0)
        for i in range(1, s_len-p_len+1):
            hash_s -= hash(s[i-1])
            hash_s += hash(s[i+p_len-1])
            if hash_s == hash_p:
                res.append(i)

        return res


def main():
    test_cases = [
        ['cbaebabacd', 'abc'],
        ['abab', 'ab'],
        ['aa', 'bb']
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.findAnagrams(test_case[0], test_case[1]))

    print('\nSolution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.findAnagrams(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
