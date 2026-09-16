#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N; cin >> N;
    if (N == 1) {cout << "NO" << endl; return;}
    if (N % 2021 == 0) {cout << "YES" << endl; return;}
    if (N % 2020 == 0) {cout << "YES" << endl; return;}
    while (N % 2020 != 0) {
        N -= 2021;
        if (N < 2020) {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;

}

int main() {
    int T; cin >> T;
    while(T--) {
        solve();
    }
}
