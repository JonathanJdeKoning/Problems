#include <bits/stdc++.h>
using namespace std;
#define int long long
main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int N; cin >> N;
    int ans = 0;
    int prev; cin >> prev;
    for(int i = 0; i < N-1; i++) {
        int x; cin >> x;
        ans += max(0LL, prev-x);
        prev = max(prev, x);
    } 
    cout << ans;
}


