#include <math.h>
#include <stdio.h>
#include <string.h>

int is_palindrome(int n) {
    int len = (int)((ceil(log10(n)) + 1));
    char str[10];
    sprintf(str, "%d", n);
    for (int i = 0; i < len; i++) {
        if (str[i] != str[len - i - 1]) {
            printf("%d\n", i);
            return 0;
        }
    }
    return 1;
}

int main() {
    int largest = 0;
    for (int i = 100; i <= 999; i++) {
        for (int j = 100; j <= i; j++) {
            if (is_palindrome(i * j) == 1) {
                if (i * j > largest) {
                    largest = i * j;
                }
            }
        }
    }
    printf("%d", largest);
}