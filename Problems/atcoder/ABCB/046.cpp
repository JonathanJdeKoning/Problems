#include "dekodingTemplate.hpp"

int main() {
    INT(N); INT(K);
    int ans = K;
    FOR(N-1) { 
        ans*=(K-1);
    }
    print(ans);

}