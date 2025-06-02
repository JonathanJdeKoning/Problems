#define LOCAL
#include "dekodingTemplate.hpp"

int main() {
    INT(H); INT(W);
    FOR(H) {
        STR(S);
        print(S);
        print(S);
    }
}