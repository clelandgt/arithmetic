/** 用两个队列实现栈, 实现原理如下：
 * 入队：将元素进栈A
 * 出队：判断栈B的元素是否为空，如果为空，将栈A的所有元素pop,并push到栈B,栈B出栈;如果不为空,栈直接出栈。
*/

#include<iostream>
#include<stack>

using namespace std;

// 算法1： 使用递归解决
class Solution1 {
public:
    int Fibonacci(int n) {
        if(n <= 0) return 0;
        if(n == 1) return 1;
        return Fibonacci(n-1) + Fibonacci(n-2);
    }
};

// 算法2：使用循环解决
class Solution2 
{
public:
    int Fibonacci(unsigned int n) 
    {
        if(n == 0 || n == 1)
        {
            return n;
        }

        int nNumSubOne = 1;
        int nNumSubTwo = 0;
        int nNum = 0;
        for(int i=2; i<=n; i++)
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

    Solution2 s = Solution2();
    printf("%d", s.Fibonacci(0));
    return 1;
}

