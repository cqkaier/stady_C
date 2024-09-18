#include <stdio.h>

int main() {
    char input[100], output[100];
    int i;
    
    // 提示用户输入字符串
    printf("请输入一个字符串: ");
    scanf("%s", input);
    
    // 遍历输入字符串并进行加密
    for (i = 0; input[i] != '\0'; i++) {
        output[i] = input[i] + (i + 1);
    }
    
    // 添加字符串结束符
    output[i] = '\0';
    
    // 输出加密后的字符串
    printf("加密后的字符串是: %s\n", output);
    
    return 0;
}
