#include "dekodingTemplate.hpp"

int main() {
    string s;
    int ans = 0;
    while (cin >> s) {
        if (s.contains('r')) {ans++;}
    }
    print(ans);
}