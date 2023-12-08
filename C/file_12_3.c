#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
//-----------
//1.
//hello word
//##########
//字符两边向中间缩进
//---------------
//2.
//猜数字游戏
//3.
//goto语句
int main()
{
    char arr1[] = "hello word";
    char arr2[] = "##########";
    // int lg = sizeof(arr2)/sizeof(arr2[0]);
    // int i = 0;
    // for ( i = 0; i < lg; i++)
    // {
    //     arr2[i] = arr1[i];
    //     sleep(1);
    //     system("clear");
    //     printf("%s\n",arr2);
    //     /* code */
    // }
    int i = 0;
    // int length = sizeof(arr1)/sizeof(arr1[0]);
    int length = strlen(arr1);
    int left = 0;
    // int right = length - 2;
    int right = length - 1;
    while(left <= right)
    {
    
    arr2[left] = arr1[left];
    arr2[right] = arr1[right];
    left++;
    right--;
    // if (right < left)
    // {

    //     break;
    //     /* code */
    // }
    sleep(1);
    system("clear");
    printf("%s\n",arr2);
        /* code */
    }
    //------
    printf("-----猜数字游戏-----\n");
    //获取1-100的数字
    printf("-----   请选择   ----\n");
    printf("请选择:\n1:进入游戏\n0.exit\n");
    int input1 = 0;//获取用户进入系统输入选择的数字
    scanf("%d",&input1);
    int k = 0;//初始化猜测的数字
    switch (input1)
    {
    case 1:
        /* code */
            srand(time(NULL));
            int num =rand()%100+1;//获取一个随机数字
            printf("%d\n",num);//打印出获取到的随机数字
            printf("请输入数字:");

            while(k != num)
            {
            scanf("%d",&k);//获取用户输入猜测的数字
            if (k > num) //判断输入的数字与生成的数字比较大小
            {
                printf("数字大了!\n请在次输入:");
                /* code */
            }
            else if (k < num)
            {
                printf("数字小了!\n请在次输入:");
                /* code */
            }
            else
            {
                printf("恭喜你,猜对了!\n");
                printf("%d\n",num);

                break;
            }
            }
            
            printf("%d\n",num);
        break;
    case 0:
            printf("以退出!\n");
            break;
    default:
        printf("输入错误!\n");
        break;
    }

   
    return 0;
}





