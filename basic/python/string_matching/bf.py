# -*- coding: utf-8 -*-
# @File  : bf.py
# @Author: clelandgt@163.com
# @Date  : 2019-10-15
# @Desc  :
from time import time


def bf(main, pattern):
    n = len(main)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == main else -1

    for i in range(n-m+1):
        for j in range(m):
            if main[i+j] == pattern[j]:
                if j == m-1:
                    return i
                else:
                    continue
            else:
                break
    return -1


def main():
    m_str = 'a' * 100000
    p_str = 'a' * 200 + 'b'

    t = time()
    print('---------- performance ----------')
    print('[bf] result:', bf(m_str, p_str))
    print('[bf] time cost: {0:.5}s'.format(time()-t))


    m_str = 'thequickbrownfoxjumpsoverthelazydog'
    p_str = 'jump'
    t = time()
    print('---------- search ----------')
    print('[bf] result:', bf(m_str, p_str))
    print('[bf] time cost: {0:.5}s'.format(time()-t))


if __name__ == '__main__':
    main()
