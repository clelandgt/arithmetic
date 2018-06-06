/** 打印从1到最大的n位数
 * 问题：输入数字n,按顺序打印出从1到最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的三位数999
 * 解法：该题应注意两点：1. n>0; 2. n位数可能是大数；
*/

#include<iostream>

using namespace std;


class Solution
{
public:

    //算法(不适用于大数): 得到最大值max，然后再从1开始遍历打印到max
    int Print1ToMaxOfNDigit1(int n)
    {   
        if(n<=0)
            return -1;
        
        unsigned int unMax = 1;
        while(n>0)
        {
            unMax *= 10;
            n--;
        }
        unMax -= 1;

        for(unsigned int i=1; i<=unMax; i++)
        {
            printf("%d,", i);
        }
        return 0;
    }

    //算法(适用于大数): 使用字符串模拟大数
    int Print1ToMaxOfNDigit2(int n)
    {   
        if(n<=0)
            return -1;
        
        char* pcNumber = new char[n+1];
        memset(pcNumber, '0', n);
        pcNumber[n] = '\0';

        while(!Increment(pcNumber))
        {
            PrintNumber(pcNumber);
            printf(",");
        }
        
        delete []pcNumber;

    }

    // 用字符串模拟大数+1
    int Increment(char* pcNumber)
    {
        bool bIsOverflow = false;
        unsigned int unTakeOver = 0;
        unsigned int unNumberLen = strlen(pcNumber);
        for(int nIndex=unNumberLen-1; nIndex>=0; nIndex--)
        {
            unsigned int unSum = pcNumber[nIndex] - '0' + unTakeOver;
            if(nIndex == unNumberLen-1)
                unSum += 1;
            if(unSum < 10)
            {
                pcNumber[nIndex] = '0' +  unSum;
                break;
            } 
            else
            {
                pcNumber[nIndex] = '0';
                unTakeOver = 1;
                if(nIndex==0)
                {
                    bIsOverflow = true;
                }
            }
        }

        return bIsOverflow;
    }
    
    // 打印字符串构成的大数，需注意'098'应打印为'98'
    void PrintNumber(char* pcNumber)
    {
        bool bIsBeginning0 = true;
        for(int nIndex=0; nIndex<=strlen(pcNumber); nIndex++)
        {
            if(pcNumber[nIndex] != '0' && bIsBeginning0)
                bIsBeginning0 = false;
            
            if(!bIsBeginning0)
                printf("%c", pcNumber[nIndex]);
        }
    }
};


int main(int argc, char* argv[])
{   
    Solution s = Solution();
    // 测试1: n<=0
    s.Print1ToMaxOfNDigit2(-3);
    // 测试1: n>0
    s.Print1ToMaxOfNDigit2(5);
    return 0;
}

