#include <stdio.h>
#include <string.h>
//模拟用户登陆
int main()
{
    printf("%ld\n",sizeof(char));
    char pass[] = "1433223a";
    printf("请输入密码：");
    char password[20] = {0};
    int i = 0;
    for ( i = 0; i < 3; i++)
    {
        /* code */
    scanf("%s",password);
    
    // if (password == pass)
    if (strcmp(password,pass) == 0)
    {
        printf("登陆成功!");
        break;
        /* code */
    }
    else
    {
    printf("密码错误！");
    }
    }
    // system("ls && ./test");
    if (i == 3)
    {
        printf("登陆失败，退出程序!");
        /* code */
    }
    
    return 0;
}