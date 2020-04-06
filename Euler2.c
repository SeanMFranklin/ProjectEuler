#include <stdio.h>

int main() {
    int sum = 0;
    int a = 1;
    int b = 1;
    int c;
    while (b < 4000000) {
        c = a;
        a = b;
        b = b + c;
        if (b % 2 == 0) {
            sum += b;
        }
    }
    printf("Sum: %d\n", sum);
}