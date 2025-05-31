#include "dekodingTemplate.hpp"

int main() {
    STR(s);
    unordered_map<char, int> mp;
    for(char c : s) {
        mp[c]++;
    }

    for (int v : views::values(mp)) {
        if (v%2 == 1) {
            print("No"); exit(0);
        }
    }
    print("Yes");
}