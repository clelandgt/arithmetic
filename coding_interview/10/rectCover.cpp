/** 矩阵覆盖
 * 问题：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
 * 解法：假设n=8,从左边开始，有两种选择：1. 竖着放，剩余7个小矩阵，有f(7)种放置方法； 2. 横着放，还得花费一个小矩阵去横着放(因为大矩阵为2*n)，剩余6个矩阵，有f(6)种放置方法。即f(8)=f(6)+f(7)
 * 当n=1时，只能竖着放f(1)=1; 当n=2时, 可以都横着放和都竖着放2种,f(2)=2; 
 * 综合上述：f(n) = f(n-1) + f(n=2); f(1) = 1; f(2) = 2
 * 
*/

#include<iostream>
#include<stack>

using namespace std;


// 算法：使用循环解决
class Solution
{
public:
    int rectCover(unsigned int n) 
    {
        if(n == 0)
        {
            return 0;
        }
        else if(n == 1)
        {
            return 1;
        }
        else if(n == 2) 
        {
            return 2;
        }

        int nNumSubOne = 2;
        int nNumSubTwo = 1;
        int nNum = 0;
        for(int i=3; i<=n; i++)
        {
            nNum = nNumSubOne + nNumSubTwo;
            nNumSubTwo = nNumSubOne;
            nNumSubOne = nNum;
        }
        return nNum;
    }
};


int main(int argc, char* argv[])
{   
    Solution s = Solution();
    printf("%d", s.rectCover(5));
    return 1;
}

