#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M; cin >> N >> M;
    int l =0 ;
    int r = 0;
    while(N--) {
        int x; cin >> x;
        l += x;
    }

    while(M--) {
        int x; cin >> x;
        r += x;
    }

    if (l == r) {
        cout << "either";
    } else if (l < r) {
        cout << "left";
    } else {
        cout << "right";
    }
}
