#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N, K; cin >> N >> K;
    vector<int> A;
    for (int i  = 0 ; i < N;i++) {
        int x; cin >> x;
        A.push_back(x);
    }
    sort(A.begin(), A.end());
    int mx = 1;
    int l = 0;
    int r;
    int curr;
    while (l < N-1) {
        curr = 1;
        for (r = l+1; r < N; r++) {
            if (A[r] - A[r-1] <= K) {
                curr++;
            } else {
                break;
            }
        }
        l = r;
        mx = max(mx, curr);
    }
    cout << N - mx << endl;
}

int main() {
    int T; cin >> T;
    while(T--) {
        solve();
    }
}
