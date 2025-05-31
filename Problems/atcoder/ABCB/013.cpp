#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    INT(M);
    int  mn = min(N, M);
    int mx = max(N,M);
    print(min(mx-mn, mn + (10-mx)));
}