#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int N; cin >> N;
    int M = 1000000007;
    int ans = 1;
    for (int i = 0; i < N;i++) {
        ans <<= 1;
        ans %= M;
    }
    cout << ans;
}


