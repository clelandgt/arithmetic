/** 解法：其实这就是个变种的斐波拉切数列。符合F(n)=F(n-1)+F(n-2) F(1)=1,F(2)=2
 *
*/

#include<iostream>
#include<stack>

using namespace std;


// 算法：使用循环解决
class Solution
{
public:
    int jumpFloor(unsigned int n) 
    {
        if(n <= 1)
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
    // Solution1 s = Solution1();
    // printf("%d", s.Fibonacci(39));

    Solution s = Solution();
    printf("%d", s.jumpFloor(1));
    return 1;
}

