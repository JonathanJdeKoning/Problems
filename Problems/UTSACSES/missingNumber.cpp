#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int N; cin >> N;
    unordered_set<int> seen;
    for (int i = 0; i < N-1; i++) {
        int x; cin >> x;
        seen.insert(x);
    }

    for (int i = 1; i <= N; i++) {
        if (not seen.count(i)) {
            cout << i; return 0;
        }
    }
}


