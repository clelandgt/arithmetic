#include <iostream>
#include "delete_repeat_node.h"

void Test1()
{
    ListNode* pNode1 =  CreateListNode(1);
    ListNode* pNode2 =  CreateListNode(2);
    ListNode* pNode3 =  CreateListNode(3);
    ListNode* pNode33 =  CreateListNode(3);
    ListNode* pNode4 =  CreateListNode(4);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode33);
    ConnectListNodes(pNode33, pNode4);


    PrintList(pNode1);
    DeleteRepeatNode(&pNode1);
    printf("After Delete Repeat Node: \n");
    PrintList(pNode1);
}

void Test2()
{
    ListNode* pNode1 =  CreateListNode(1);
    ListNode* pNode2 =  CreateListNode(1);
    ConnectListNodes(pNode1, pNode2);

    PrintList(pNode1);
    DeleteRepeatNode(&pNode1);
    printf("After Delete Repeat Node: \n");
    PrintList(pNode1);
}

void Test3()
{
    ListNode* pNode1 =  CreateListNode(1);
    ListNode* pNode2 =  CreateListNode(2);
    ListNode* pNode3 =  CreateListNode(3);
    ListNode* pNode4 =  CreateListNode(4);
    ListNode* pNode44 =  CreateListNode(4);
    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode44);

    PrintList(pNode1);
    DeleteRepeatNode(&pNode1);
    printf("After Delete Repeat Node: \n");
    PrintList(pNode1);
}

int main() {
    printf("******Test1:\n");
    Test1();

    printf("******Test2:\n");
    Test2();

    Test3();
    printf("******Test3:\n");
    return 0;
}