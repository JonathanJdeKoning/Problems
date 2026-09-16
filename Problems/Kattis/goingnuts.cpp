#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    int ans = 0;
    while(N) {
        ans += N & 1;
        N >>= 1;
    }
    cout << ans;
}
