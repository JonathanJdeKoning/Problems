#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    long long N; cin >> N;
    while(N != 1) {
        cout << N << " ";
        N = (N&1 ? N*3+1 : N/2);
    }
    cout << 1;
}


