#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K; cin >> N >> K;
    while(N--) {
        int x; cin >> x;
        if (K >= x) {
            K -= x;
            cout << "1";
        } else {
            cout << "0";
        }
    }
}
