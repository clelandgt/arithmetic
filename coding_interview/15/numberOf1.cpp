/** 二进制中1的个数
 * 问题：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
 * 
*/

#include<iostream>
#include<stack>

using namespace std;


// 算法描述(不可取)：向右移位运算，但是对于负数存在问题。如：Ox80000000右移一位后变为OxC0000000,而不是Ox40000000，接着移动，数字最终会变为OxFFFFFFFF，并一直死循环。
class Solution1
{
public:
    int NumberOf1(int n) 
    {
        int count=0;
        while(n>0)
        {
            if(n & 1)
            {
                count++;
            }
            n = n >> 1;
        }
        return count;
    }
};

// 算法描述(不可取)：向右移位运算，但是对于负数存在问题。如：Ox80000000右移一位后变为OxC0000000,而不是Ox40000000，接着移动，数字最终会变为OxFFFFFFFF，并一直死循环。
class Solution2
{
public:
    int NumberOf1(unsigned int n) 
    {
        unsigned int flag = 1;
        int count = 0;
        while(flag)
        {
            if(n & flag)
            {
                count++;
            }
            flag = flag << 1;
        }
        return count;

    }
};



int main(int argc, char* argv[])
{   
    Solution2 s = Solution2();
    printf("%d", s.NumberOf1(7));
    return 1;
}

