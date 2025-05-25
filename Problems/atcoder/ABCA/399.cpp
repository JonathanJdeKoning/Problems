#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    STR(S);
    STR(T);
    int cnt = 0;
    FOR(i, N) {
        if (S[i] != T[i]) cnt++;
    }
    print(cnt);
}