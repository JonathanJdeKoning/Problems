#include "dekodingTemplate.hpp"

int main() {
    VEC(int, A, 2);
    VEC(int, B, 2);
    YES(B[0] == A[0] or B[0] == A[1] or B[1] == A[0] or B[1] == A[1]);
}