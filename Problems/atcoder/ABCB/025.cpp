#include "dekodingTemplate.hpp"

int main() {
    INT(N); INT(MN); INT(MX);
    int pos = 0;
    FOR(N) {
        STR(S); INT(X);
        if (S[0] == 'E') {pos += clamp(X, MN, MX);}
        if (S[0] == 'W') {pos -= clamp(X, MN, MX);}
    }
    if (pos > 0) {cout << "East ";}
    if (pos < 0) {cout << "West ";}
    cout << abs(pos) << endl;
}