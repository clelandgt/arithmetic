# -*- coding: utf-8 -*-
# @File  : longest_substring_without_repeating_characters.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-26
# @Desc  : https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """暴力求解
        时间复杂度 O(n^2)
        空间复杂度 O(1)
        """
        if len(s) == 0 or not s:
            return 0

        max_len = 1
        for i in range(len(s)):
            index = 1
            for j in range(i+1, len(s)):
                # i~j 区间内，是否有重复
                if len(s[i:j+1]) == len(set((s[i:j+1]))):
                    index += 1
                else:
                    break

            if index > max_len:
                max_len = index
        return max_len


def main():
    test_cases = ["abcabcbb", "bbbbb", "pwwkew"]

    s = Solution1()
    print('***** Solution1 *****')
    for case in test_cases:
        print(f"{case}: {s.lengthOfLongestSubstring(case)}")


if __name__ == '__main__':
    main()
