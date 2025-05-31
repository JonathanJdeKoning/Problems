#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    set<int> seen;
    int ans = 0;
    FOR(N) {
        INT(X);
        if (seen.contains(X) )
            ans++;
        seen.insert(X);
    }
    print(ans);
}