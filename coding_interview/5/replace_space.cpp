#include <cstring>
#include<iostream>   
using namespace std;  


void ReplaceSpace(char *str, int length)
/*
    - string[]: 需要替换的字符串
    - length: 分配的字符数据string的总容量
*/
{
    if(str == nullptr || length <= 0)
        return;
    
    // 获取到字符创实际的长度和空格数
    int originaLenght = 0;
    int numberOfBlank = 0;
    int i = 0;
    while(str[i]!='\0')
    {
        originaLenght++;
        if(str[i]==' ')
            ++numberOfBlank;
        i++;
    }

    int newLenght = originaLenght + numberOfBlank * 2;
    if (newLenght > length)
        return;

    // 遍历替换其中的空格
    int indexOfOrigina = originaLenght;
    int indexOfNew = newLenght;
    while(indexOfOrigina >= 0 && indexOfNew > indexOfOrigina)
    {
        if(str[indexOfOrigina] == ' ')
        {
            str[indexOfNew--] = '0';
            str[indexOfNew--] = '2';
            str[indexOfNew--] = '%';
        } 
        else
        {
            str[indexOfNew--] = str[indexOfOrigina];
        }
        indexOfOrigina--;
    }

};


void Test(char* testName, char str[], int length, char expected[])
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    ReplaceSpace(str, length);

    if(expected == nullptr && str == nullptr)
        printf("passed.\n");
    else if(expected == nullptr && str != nullptr)
        printf("failed.\n");
    else if(strcmp(str, expected) == 0)
        printf("passed.\n");
    else
        printf("failed.\n");
}

// ¿Õ¸ñÔÚ¾ä×ÓÖÐ¼ä
void Test1()
{
    const int length = 100;

    char str[length] = "hello world";
    Test("Test1", str, length, "hello%20world");
}

// ¿Õ¸ñÔÚ¾ä×Ó¿ªÍ·
void Test2()
{
    const int length = 100;

    char str[length] = " helloworld";
    Test("Test2", str, length, "%20helloworld");
}

// ¿Õ¸ñÔÚ¾ä×ÓÄ©Î²
void Test3()
{
    const int length = 100;

    char str[length] = "helloworld ";
    Test("Test3", str, length, "helloworld%20");
}

// Á¬ÐøÓÐÁ½¸ö¿Õ¸ñ
void Test4()
{
    const int length = 100;

    char str[length] = "hello  world";
    Test("Test4", str, length, "hello%20%20world");
}

// ´«Èënullptr
void Test5()
{
    Test("Test5", nullptr, 0, nullptr);
}

// ´«ÈëÄÚÈÝÎª¿ÕµÄ×Ö·û´®
void Test6()
{
    const int length = 100;

    char str[length] = "";
    Test("Test6", str, length, "");
}

//´«ÈëÄÚÈÝÎªÒ»¸ö¿Õ¸ñµÄ×Ö·û´®
void Test7()
{
    const int length = 100;

    char str[length] = " ";
    Test("Test7", str, length, "%20");
}

// ´«ÈëµÄ×Ö·û´®Ã»ÓÐ¿Õ¸ñ
void Test8()
{
    const int length = 100;

    char str[length] = "helloworld";
    Test("Test8", str, length, "helloworld");
}

// ´«ÈëµÄ×Ö·û´®È«ÊÇ¿Õ¸ñ
void Test9()
{
    const int length = 100;

    char str[length] = "   ";
    Test("Test9", str, length, "%20%20%20");
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();
    Test8();
    // Test9();

    return 0;
}

