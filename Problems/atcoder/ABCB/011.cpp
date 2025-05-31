#include "dekodingTemplate.hpp"

int main() {
    STR(S);
    cout << (char)toupper(S[0]);
    for (char c: S.substr(1, S.size()-1)) {
        cout << (char)tolower(c);
    }
    cout << endl;
}