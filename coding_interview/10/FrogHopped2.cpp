/** 变态跳台阶
 * 问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
 * 解法：
 *  当n=1时：只有一种跳法f(1)=1;
 *  当n=2时：第一次跳1阶的跳法为f(2-1),跳2阶为f(2-2).总为f2=f1+f0;
 *  当n=3时：第一次跳1阶的跳法为f(3-1),跳2阶为f(3-2),跳3阶为f(3-3).总为f3=f2+f1+f0;
 *  当n=n时：第一次跳1阶的跳法为f(n-1),跳2阶为f(3-2),跳3阶为f(3-3),跳n阶为f(n-n).  总为fn=f(n-1)+f(n-2)+..+f(1)+f(0);
 *  使用归纳法推导：由f(n)=f(0)+f(1)+f(2)..+f(n-2)+f(n-1), f(n-1)=f(0)+f(1)+f(2)..+f(n-2)，可推导f(n)=2(f(n-1)).可得到推导式如下：
 *  f(n) = 1, (n=0)
 *  f(n) = 1, (n=1)
 *  f(n) = 2(f(n-1)), (n=n)
*/

#include<iostream>
#include<stack>

using namespace std;


// 算法：使用循环解决
class Solution
{
public:
    int jumpFloorII(unsigned int n) 
    {
        if(n <= 0)
        {
            return 1;
        }
        else if(n == 1) 
        {
            return 1;
        }

        int nNumSubOne = 1;
        int nNum = 0;
        for(int i=2; i<=n; i++)
        {
            nNum = 2 * nNumSubOne;
            nNumSubOne = nNum;
        }
        return nNum;
    }
};


int main(int argc, char* argv[])
{   
    Solution s = Solution();
    printf("%d", s.jumpFloorII(3));
    return 1;
}

