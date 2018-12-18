/** 用两个队列实现栈, 实现原理如下：
 * 入队：将元素进栈A
 * 出队：判断栈B的元素是否为空，如果为空，将栈A的所有元素pop,并push到栈B,栈B出栈;如果不为空,栈直接出栈。
*/

#include<iostream>
#include<stack>

using namespace std;

class Solution
{
public:
    void push(int node) 
    {
        stack1.push(node);
    }

    int pop() {
        if(stack2.empty())
        {
            while(!stack1.empty())
            {
                int num = stack1.top();
                stack2.push(num);
                stack1.pop();
            }
            int result = stack2.top();
            stack2.pop();
            return result;
        }
        else
        {
            int result = stack2.top();
            stack2.pop();
            return result;
        }

    }

private:
    stack<int> stack1;
    stack<int> stack2;
};


int main(int argc, char* argv[])
{   
    Solution s = Solution();
    std::printf("push some numbers(4,5,6)\n");
    s.push(4);
    s.push(5);
    s.push(6);
    std:printf("pop numbers:\n");
    std::printf("%d", s.pop()); 
    std::printf("%d", s.pop());
    std::printf("%d", s.pop());

    return 1;
}