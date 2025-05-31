#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    INT(MASK);
    VEC(int, A, N);
    int total= 0;
    int currBit = 0;
    while (currBit < len(A)) {
        total += A[currBit] * (MASK & 1);
        MASK >>= 1;
        currBit++;
    }
    print(total);
}