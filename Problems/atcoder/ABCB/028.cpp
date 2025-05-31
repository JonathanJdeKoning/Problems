#include "dekodingTemplate.hpp"

int main() {
    STR(S);
    unordered_map<char, int> mp;

    for (auto c : S) {
        mp[c]++;
    }
    cout << mp['A'] << ' ' << mp['B'] <<  ' ' << mp['C'] << ' ' << mp['D'] << ' ' << mp['E'] <<  ' ' << mp['F'] << endl;
}