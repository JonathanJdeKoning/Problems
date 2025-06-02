#define LOCAL
#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    VEC(int, A, N);
    INT(M);
    int total = accumulate(all(A), 0);

    FOR( i, M) {
        INT(P); INT(X);
        cout << total - A[P-1] + X << '\n';
    }
}