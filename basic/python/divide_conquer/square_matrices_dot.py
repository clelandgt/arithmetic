# -*- coding: utf-8 -*-
# @File  : square_matrices_dot.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-11
# @Desc  :
import numpy as np


def timeit(method):
    import time

    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()
        spend_time = int((end_time - start_time) * 1000)
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = spend_time
        else:
            print('{0}: {1} ms'.format(method.__name__, spend_time))

        return result
    return timed


@timeit
def square_matrices_dot1(n1, n2):
    """循环遍历解决"""
    if len(n1) != len(n2):
        return
    size = len(n1)

    result = []
    # n1行遍历
    for i in range(size):
        result_row = []
        # n2列遍历
        for j in range(size):
            item_sum = 0
            for z in range(size):
                item_sum += n1[i][z] * n2[z][j]
            result_row.append(item_sum)
        result.append(result_row)

    return result


def main():
    n1 = np.random.randint(1, 100, 25).reshape(5, 5)
    n2 = np.random.randint(1, 100, 25).reshape(5, 5)
    print('标准答案: {}'.format(np.dot(n1, n2)))

    n1 = n1.tolist()
    n2 = n2.tolist()
    print('CASE1 Result: ', square_matrices_dot1(n1, n2))


if __name__ == '__main__':
    main()
