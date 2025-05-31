#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    VEC(int,A, N);
    sort(all(A));
    reverse(all(A));
    double total = 0;
    double pi = 3.1415926535;
    FOR(i, N) {
        int r = A[i];
        double size = r*r*pi;
        if (i%2==0) {
            total += size;
        } else {
            total -= size;
        }
    }
    cout << total;
}