#include <bits/stdc++.h>
using namespace std;

void solve() {
    deque<int> q;
    deque<int> r;
    int N; cin >> N;
    
    long long sum = 0;
    long long rizz = 0;
    long long revrizz = 0;

    for (int i = 0; i < N; i++) {
        int op; cin >> op;
        if (op == 1) {
            // REG
            rizz -= q.back() * q.size();
            rizz += sum;
            q.push_front(q.back());
            q.pop_back();
            //REV
            revrizz += r.size() * r.front();
            revrizz -= sum;
            r.push_back(r.front());
            r.pop_front();

        } else if (op == 2) {
            swap(rizz, revrizz);
            swap(q, r);
        } else if (op == 3) {
            int x; cin >> x;
            //REG
            q.push_back(x);
            rizz += x * q.size();
            //REV
            r.push_front(x);
            revrizz += sum + x;

            sum += x;
        }
        cout << rizz << '\n';
    }
}

int main() {
    int T; cin >> T;
    while(T--) {
        solve();
    }
}
