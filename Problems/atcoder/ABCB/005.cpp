#include "dekodingTemplate.hpp"
int main() {
    INT(N);
    vi A;
    FOR(N) {
        INT(x);
        A.eb(x);
    }
    print(MIN(A));
}
