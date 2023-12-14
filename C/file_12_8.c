#include <stdio.h>
#include "add.h"
//声明定义函数
int main()
{
    int a = 0;
    int b = 0;
    scanf("%d %d",&a,&b);//获取用户输入
    int sum = Add(a,b);//调用Add函数，将a,b传给Add函数
    printf("%d\n",sum);
    
    return 0;
}