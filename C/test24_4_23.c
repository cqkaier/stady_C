#include <stdio.h>

int main() {
    char a = 'T';
    char b = 'c';

    printf("Before swap: a = %c, b = %c\n", a, b);

    // 不使用临时变量直接交换字符变量的值
    a = a ^ b; // a现在包含a和b的异或结果
    b = a ^ b; // b现在被还原为原来的a
    a = a ^ b; // a现在被还原为原来的b

    printf("After swap: a = %c, b = %c\n", a, b);

    return 0;
}

