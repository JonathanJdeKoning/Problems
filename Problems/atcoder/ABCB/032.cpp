#include "dekodingTemplate.hpp"
int main() {
    STR(S);
    INT(K);
    int l = 0;
    set<string> seen;
    while (l+K <= len(S)) {
        seen.insert(S.substr(l, K));
        l++;
    }
    print(len(seen));
}
