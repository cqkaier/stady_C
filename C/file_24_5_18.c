#include <stdio.h>

int main() {
    int divisor = 1;
    char[100] num;

    printf("请输入一个正整数:");
    scanf("%s", &num);

    // 计算出最大的10的幂次
    while ((int)num / divisor >= 10) {
        divisor *= 10;
    }

    // 按高位到低位输出各位数字
    while (divisor >= 1) {
        printf("%d ", ((int)num / divisor) % 10);
        divisor /= 10;
    }
    printf("\n");

    return 0;
}
