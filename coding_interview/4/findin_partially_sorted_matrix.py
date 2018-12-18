# -*- coding:utf-8 -*-



class Solution1:
    """全遍历 效率最低
    """

    def Find(self, target, array):
        for item in array:
            if target in item:
                return True
        return False


class Solution2:
    """效率高
    该矩阵是有序的(从左下角来看，向右数字递增，向上数字递减)。因此从左下角开始查找，当要查找的数比左下角的数大时，右移; 当要查找的数比左下角的数小时，上移。
    """
    def Find(self, target, array):
        row_num = len(array)
        col_num = len(array[0])
        is_found=False

        for col_index in xrange(col_num):
            row_index = row_num - 1
            if target == array[row_index][col_index]:
                is_found = True
                break
            elif target > array[row_index][col_index]:
                continue
            else:
                while(row_index>0):
                    row_index -= 1
                    if target == array[row_index][col_index]:
                        is_found = True
                        break
                    if target > array[row_index][col_index]:
                        break

        return is_found


if __name__ == '__main__':
    # s1 = Solution1()
    # print s1.Find([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]], 17)

    s2 = Solution2()
    print s2.Find(17, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
