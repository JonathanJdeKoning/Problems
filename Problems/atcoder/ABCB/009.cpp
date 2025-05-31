#include "dekodingTemplate.hpp"
int main() {
    INT(N);
    vi A;
    FOR(N) {
        INT(P);
        A.eb(P);
    }
    UNIQUE(A);
    print(*max_element(A.begin(), A.end() - 1));
}
