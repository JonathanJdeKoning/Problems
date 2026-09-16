#include <bits/stdc++.h>
using namespace std;

string solve() {
    int N, A, B; cin >> N >> A >> B;
    if (A + B == N*2) 
        return "Yes\n";
    if (A + B < (N-1)) {
        return "Yes\n";
    }
    return "No\n";
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int T; cin >> T;
    while(T--) {
        cout << solve();
    }
}


