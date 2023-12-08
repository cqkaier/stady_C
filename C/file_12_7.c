#include <stdio.h>
int is_sushu(int n)
{
    int j = 0;
    for ( j = 2; j < n-1; j++)
    {
        if ( n % j == 0)
        {
            return 0;
            /* code */
        }
        
        /* code */
    }
    return 1;
}
int leap_year(int year)
{
    if (year%4 == 0)
    {
        if (year%100 != 0)
        {
            return 1;
            /* code */
        }
        
        /* code */
    }
    if (year%400 ==0)//这里不能用else if ，因为if执行之后else就不会在执行了
    {
        return 1;
        /* code */
    }
    else
    {
        return 0;
    }
    
    
}
void test(void)//test(void)，这个void是声明不接收参数
{
    printf("hehe\n");
}
void test1()
{
    test();//该函数嵌套调用test函数
    printf("haha\n");
}
int main()
{
    //素数只能被1和自身整除
    //不是素数的一个数分解为两个数相乘其中一定有一个数<=这个数开平方的值
    //判断100-200之间的素数
    int num1 = 0;
    int a = 0;
    for ( num1 = 100; num1 < 201; num1++)//产生100-200之间的数字
    {
        // printf("%d ",num1);//验证产生的100-200之间的数字
        if (is_sushu(num1))
        {
            a++;
            printf("%d ",num1);
        }
        /* code */
    }
    printf("个数为:%d\n",a);
    //判断1000-2000年之间的闰年
    //判断闰年(leap_year)的两种方法
    //1.能被4整除并且不能被100整除的
    //2.能被400整除的
    int year = 0;
    int b = 0;//用于统计个数，初始化
    for ( year = 1000; year < 2001; year++)//获取1000-2000的数字
    {
        // printf("%d ",year);//打印1000-2000的数字
        // if (((year%4==0)&&(year%100!=0))||(year%400==0))
        // {
        //     b++;
        //     printf("%d ",year);
        //     /* code */
        // }//这是普通写法
        int lp = leap_year(year);
        if (lp == 1)
        {
            b++;
            printf("%d ",year);
            /* code */
        }//这是调用函数写法
        
        /* code */
    }
    printf("闰年个数为:%d\n",b);
    //定义函数用半折法查找数组中的元数
//现在还不想写

    //函数的嵌套调用

test1();
    return 0;
}