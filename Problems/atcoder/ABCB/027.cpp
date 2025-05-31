#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    VEC(int, A, N);
    int total = accumulate(all(A), 0 );

    if (total% N != 0) {print(-1); exit(0);}
    int need = total / N;
    int ans = 0;

    int currSum = 0;
    int currLen = 0;
    FOR(i, N) {
        currSum += A[i];
        currLen += 1;

        if (currSum % currLen != 0 or currSum / currLen != need) {
            ans++;
        } else {
            currSum = 0;
            currLen = 0;
        }
    }
    print(ans);
}