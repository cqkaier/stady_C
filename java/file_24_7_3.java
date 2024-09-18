public class file_24_7_3 {
    public static void main(String[] args) {
        int[] a = {10, 50, 5, 9, 1};
        for (int i = 0; i < 4; i++) { // 只需要遍历到倒数第二个元素
            for (int j = 0; j < 5 - i - 1; j++) { // 确保j + 1不会超出数组界限
                if (a[j] > a[j + 1]) {
                    int t = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = t;
                }
            }
        }
        for (int c = 0; c < 5; c++) {
            System.out.println(a[c]);
        }
    }
}

