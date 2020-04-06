#include <stdio.h>

int main() {
    int res = 0;
    for (int i = 1; i < 1000; i++) {
        if (i % 5 == 0 || i % 3 == 0) {
            res += i;
        }
    }
    printf("Ans: %d\n", res);
}
