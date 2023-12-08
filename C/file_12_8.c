#include <stdio.h>
#include "add.h"
int main()
{
    int a = 0;
    int b = 0;
    scanf("%d %d",&a,&b);
    int sum = Add(a,b);
    printf("%d\n",sum);
    return 0;
}