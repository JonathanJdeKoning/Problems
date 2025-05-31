#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    unordered_map<string, int> mp;

    FOR(N) {
        STR(name);
        mp[name]++;
    }
    int mx = MAX(views::values());
    for (auto k: views::keys(mp)) {
        if (mp[k] == mx) {
            print(k);
            break;
        }
    }
}
