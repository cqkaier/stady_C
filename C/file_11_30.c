#include <stdio.h>
//while   for   do   while 循环
int main()
{
    // int i = 0;
    // while (i<10)
    // {
    //     i++;
    //     if (i == 5)
    //     {
    //         // break;
    //         continue;
    //         /* code */
    //     }
        
    //     printf("%d",i);
    //     /* code */
    // }
    // int a = 0;
    // for ( a = 1; a <= 10; a++)
    // {
    //     if (a == 5)
    //     {
    //         break;
    //         // continue;
    //         /* code */
    //     }
        
    //     printf("%d",a);
    //     /* code */
    // }
    int b = 0;
    do
    {
        // b++;
        if (b == 5)
        {
            // break;
            continue;
            /* code */
        }
        // b++;//放这打印1-4然后死循环
        
        printf("%d",b);
        /* code */
    } while (b<10);
    
    
    return 0;
}