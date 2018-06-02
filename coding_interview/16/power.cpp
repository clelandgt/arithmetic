/** 数值的整数次方
 * 问题：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
 * 
*/

#include<iostream>

using namespace std;

/* 这个题目看起来比较简单，但是需要考虑到多种异常情况
1. 底数为0时，指数<0时，用户输入时无效的。指数>=0时，值都为0;
2. 指数>=0时: 结果为result;  指数<0时：值为当前的倒数1/result。
*/

class Solution
{
public:
    bool m_bInvaildInput;
    Solution(): m_bInvaildInput(false){}

    bool equal(double num1, double num2)
    {
        if ((num1 - num2 > -0.0000001) && (num1 - num2 < 0.0000001))
            return true;
        else
            return false;
    }

    double Power(double dBase, int nExponent) 
    {
        if(equal(dBase, 0.0) && (nExponent < 0))
        {
            m_bInvaildInput = true;
            return 0.0;
        }

        unsigned int unAbsExponent = nExponent;
        if(nExponent < 0)
        {
            unAbsExponent = 0 - nExponent;
        }

        double dResult = 1.0;
        for(int i=1; i<=unAbsExponent; i++)
        {
            dResult *= dBase;
        }

        return (nExponent >0) ? dResult: 1.0 / dResult;

    }
};



int main(int argc, char* argv[])
{   
    Solution s = Solution();
    if(s.m_bInvaildInput)
    {
        printf("input error\n");
        return -1;
    }
    printf("test1: %f\n", s.Power(2, 3));
    printf("test2: %f\n", s.Power(2, -3));
    printf("test3: %f\n", s.Power(0, -3));
    printf("test4: %f\n", s.Power(0, 0));
    return 0;
}

