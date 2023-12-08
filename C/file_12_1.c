#include <stdio.h>
//求n的阶乘
int main()
{
    int i = 0;
    int sum = 1;
    int n = 0;
    scanf("%d",&n);
    for ( i = 1; i <= n; i++)
    {
        
        sum = sum*i;
        
        /* code */
    }
    printf("%d\n",sum);
    printf("%d\n",1*2*3*4*5);
    printf("求1!+....+10!\n");
    
    // for ( i = 1; i <= 10; i++)
    // {
    //     printf("%d",i);
    //     sum = sum * i;
    //     for ( i = 1; i < 10; i++)
    //     {
    //         int a = sum;
            
    //         /* code */
    //     }
        
        /* code */
    // }
    //chatgpt帮改的
    sum = 0;

    for (i = 1; i <= 10; i++) {
        int factorial = 1;

        // 计算当前 i 的阶乘
        for (int j = 1; j <= i; j++) {
            factorial = factorial * j;
        }

        sum = sum + factorial;
    }

    // 输出结果
    printf("1! + 2! + ... + 10! = %d\n", sum);
    //折半算法在数组中查找arr[]=1,2,3,4,5,6,7,8,9,10
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int left = 0;
    int right = 9;
    int ret = sizeof(arr)/sizeof(arr[0]);
    int k = 7;
    while (left <= right)
    {
    int mid = (left+right)/2;

    if (arr[mid] < k)
    {
        left = mid + 1;
        /* code */
    }
    else if (arr[mid] > k)
    {
        right = mid - 1;
        /* code */
    }
    else if (arr[mid] ==k)
    {
        printf("找到了，下标为:%d\n",mid);
        break;
        /* code */
    }
    }
    if (left > right)
    {
        printf("找不到了！");
        /* code */
    }
       
    
    return 0;
}