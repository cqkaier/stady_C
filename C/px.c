#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // 交换 arr[j] 和 arr[j+1]
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int numbers[4];
    printf("请输入4个数，用空格分隔：");
    for(int i = 0; i < 4; i++) {
        scanf("%d", &numbers[i]);
    }

    bubbleSort(numbers, 4);

    printf("按从小到大的顺序输出为：");
    for(int i = 0; i < 4; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}

