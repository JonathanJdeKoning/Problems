#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    set<int> seen;
    int N; cin >> N;
    for (int i = 0; i < N;i++) {
        int x; cin >> x;
        seen.insert(x);
    }
    cout << seen.size();
}


