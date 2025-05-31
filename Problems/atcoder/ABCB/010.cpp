#include "dekodingTemplate.hpp"

int main() {
    
    INT(N);
    VEC(int, A, N);
    int ans{0};

    FOR(i, N) {
        int petal = A[i];
        if (petal%2==0) {
            ans++;
        }
        if (petal == 6) {ans += 2;}
        if (petal == 5) {ans += 2;}

    }
    print(ans);
}