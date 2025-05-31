#include "dekodingTemplate.hpp"

int main() {
    STR(S);
    for (char c : S) {
        if (c=='a' or c=='e' or c =='i' or c == 'o' or c == 'u') continue;
        cout << c;
    }
    cout << '\n';
}