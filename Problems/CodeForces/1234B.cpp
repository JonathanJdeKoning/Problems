#include <bits/stdc++.h>
using namespace std;
deque<int> q;
set<int> vis;

int main() {
    int N, K; cin >> N >> K;
    int id;

    for (int i = 0; i < N; i++) {
        cin >> id;
        if (vis.find(id) != vis.end()) {continue;}
        if (q.size() == K) {
            vis.erase(q.back());
            q.pop_back();
        }
        q.push_front(id);
        vis.insert(id);
    }
    cout << q.size() << '\n';
    for (auto x: q) {
        cout << x << " ";
    }
    cout << '\n';
}
