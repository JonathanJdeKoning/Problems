#include "dekodingTemplate.hpp"

int main() {
    INT(L);
    INT(H);
    INT(N);
    FOR(N) {
        INT(X);
        if( X > H ){print(-1); continue;}
        if( X < L ){print(L - X); continue;}
        print(0);
    }
}