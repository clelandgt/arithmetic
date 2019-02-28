#include <iostream>
#include "ReOrderArray.h"

void Test1()
{
    ListNode* pNode1 = CreateListNode(2);
    ListNode* pNode2 = CreateListNode(1);
    ListNode* pNode3= CreateListNode(3);
    ListNode* pNode4= CreateListNode(1);
    ListNode* pNode5= CreateListNode(4);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    PrintList(pNode1);
    printf("After ReOrderArray: \n");

}


int main()
{
    printf("Test1:\n");
    Test1();

    return 0;
}