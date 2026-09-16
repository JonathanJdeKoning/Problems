#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long N; cin >> N;
    if (__builtin_popcountll(N) != 1) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    int T; cin >> T;
    while(T--) { solve(); }     
}
