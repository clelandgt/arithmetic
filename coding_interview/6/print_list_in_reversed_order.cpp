#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include <stack>

using namespace std;

struct ListNode
{
    int m_nValue;
    ListNode *m_pNext;
};

ListNode* CreateListNode(int value)
{
    ListNode* pNode = new ListNode();
    pNode->m_nValue = value;
    pNode->m_pNext = nullptr;

    return pNode;
}

void ConnectListNodes(ListNode* pCurrent, ListNode* pNext)
{
    if(pCurrent == nullptr)
    {
        printf("Error to connect two node.\n");
        exit(1);
    }
    pCurrent->m_pNext = pNext;
}

void PrintListNode(ListNode* pHeader)
{
    printf("PrintList start.\n");
    ListNode* pNode = pHeader;
    while(pNode != nullptr)
    {
        printf("%d\t", pNode->m_nValue);
        pNode = pNode->m_pNext;
    }

    printf("\nPrintList ends.\n");
}

void PrintList(ListNode* pHead)
{
    printf("PrintList starts.\n");
    
    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        printf("%d\t", pNode->m_nValue);
        pNode = pNode->m_pNext;
    }

    printf("\nPrintList ends.\n");
}

void DestoryList(ListNode* pHeader)
{
    ListNode* pNode = pHeader;
    while(pNode != nullptr)
    {
        pHeader = pHeader->m_pNext;
        delete pNode;
        pNode = pHeader;
    }
}


/* 
解决方案一：利用栈的后进先出
    利用栈后进先出的特性，遍历链表存入栈。然后再出栈打印数据
*/
void PrintListFromTailToHeader(ListNode * pHeader)
{
    std::stack<ListNode*> nodes;
    ListNode *pNode = pHeader;

    while(pNode!=nullptr)
    {
        nodes.push(pNode);
        pNode=pNode->m_pNext;
    }

    while(!nodes.empty())
    {
        pNode = nodes.top();
        printf("%d\t", pNode->m_nValue);
        nodes.pop();
    }

}

/** 解决方案二：利用递归实现
 * 
*/

void printListReversingly_Recursively(ListNode* pHead)
{
    if(pHead != nullptr)
    {
        if(pHead->m_pNext != nullptr)
        {
             printListReversingly_Recursively(pHead->m_pNext);
        } 
        printf("%d\n", pHead->m_nValue);
    }
}

void Test(ListNode* pHead)
{
    PrintList(pHead);
    PrintListFromTailToHeader(pHead);
    printf("\n");
    PrintListFromTailToHeader(pHead);
}

void Test2(ListNode* pHead)
{
    PrintList(pHead);
    printListReversingly_Recursively(pHead);
}


// 1->2->3->4->5
void Test1()
{
    printf("\nTest1 begins.\n");

    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    Test(pNode1);

    // DestroyList(pNode1);
}

int main(int argc, char* argv[])
{   
    Test1();
}