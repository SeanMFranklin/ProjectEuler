#include <stdio.h>

int main() {
    long long n = 600851475143;
    long int i = 2;
    while (i * i < n) {
        if (n % i == 0) {
            n /= i;
        } else {
            i += 1;
        }
    }
    printf("Ans: %d", (int)n);
}
