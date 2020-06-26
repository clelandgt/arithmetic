# -*- coding: utf-8 -*-
# @File  : group_anagrams.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-27
# @Desc  :
from typing import List
import collections


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for item in strs:
            k = ''.join(sorted(item))
            if k not in result:
                result[k] = []
            result[k].append(item)

        return result.values()


def main():
    test_cases = [["eat", "tea", "tan", "ate", "nat", "bat"]]

    print('***** Solution1 *****')
    s = Solution1()
    for test_case in test_cases:
        print(s.groupAnagrams(test_case))




if __name__ == '__main__':
    main()
