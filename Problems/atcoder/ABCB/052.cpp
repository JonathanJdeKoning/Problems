#define LOCAL
#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    STR(S);
    int x =0 ;
    int mx = 0;
    for(auto c: S) {
        if (c=='I') {x++; mx = max(x, mx);}
        else {x--;}
    }
    print(mx);
}