#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N; cin >> N;
    int ans = 0;
    while(N != 1) {
        if (N%3 !=0 ) {cout << -1 << endl; return;}
        ans++;
        if (N % 6 == 0) {
            N/= 6;
        } else {
            N *= 2;
        }
    }   
    cout << ans << endl; 
}

int main() {
    int T; cin >> T;
    while(T--) {
        solve();
    }
}
