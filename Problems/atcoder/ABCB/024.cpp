#include "dekodingTemplate.hpp"

int main() {
    INT(N); INT(K);
    int ans = 0;
    INT(prev);
    FOR(N-1) {
        INT(T);
        if (T - prev <= K) {
            ans += T - prev;
        } else {
            ans += K;
        }
        prev = T;
    }
    print(ans + K);
}