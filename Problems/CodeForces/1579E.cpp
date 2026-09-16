#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N; cin >> N;
    deque<int> q;
    for (int i = 0; i < N; i++) {
        int x; cin >> x;
        if (q.size() == 0) {q.push_back(x); continue;}
        if (x < q.front()) {
            q.push_front(x);
        } else {
            q.push_back(x);
        }
    }
    for (int x : q) {
        cout << x << " ";
    }
    cout << '\n';
}

int main() {
    int T; cin >> T;
    while (T--) {
        solve();
    }
}
