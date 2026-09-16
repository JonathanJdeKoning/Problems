#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N; cin >> N;
    vector<int> A(N);
    for(int i =0; i<N;i++) cin >> A[i];
    if (N % 2 == 0) {
        cout << "2\n";
        cout << "1 " << N << '\n';
        cout << "1 " << N << '\n';
        return;
    } else {
        cout << "4\n";
        cout << "1 " << N <<'\n';
        cout << "2 " << N << '\n';
        cout << "1 2\n";
        cout << "1 2\n";
    }
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int T; cin >> T;
    while(T--) {
        solve();
    }
}


