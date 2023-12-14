#include <stdio.h>
#include <string.h>
//从1开始逐个输出1234用函数递归实现
void print(unsigned int sum)
{
    if (sum > 9)
    {
        print(sum/10);
        printf("%d ",sum%10);
    }
    else{
    printf("%d ",sum%10);
}
}
int my_strlen(char *str)
{
    if (*str != '\0')
    {
        return 1+my_strlen(str+1);
        /* code */
    }
    else
    {
        return 0;
    }
    
}
int main()
{
    unsigned int num = 0;//初始化numw无符号整形
    scanf("%u",&num);//获取用户输入
    print(num);//调用print函数
    //求字符串长度，运用函数递归
    char arr[] = "abc";
    printf("%ld\n",strlen(arr));
    printf("\n");
    int len = my_strlen(arr);
    printf("%d\n",len);
    return 0;
}