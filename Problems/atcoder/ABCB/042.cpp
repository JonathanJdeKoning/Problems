#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    INT(K);
    vector<string> A;
    FOR(N) {
        STR(s);
        A.eb(s);
    }
    sort(all(A));
    for (string s : A) {
        cout << s;
    }
    cout << endl;
}