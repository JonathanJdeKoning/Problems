#include <bits/stdc++.h>
using namespace std;

int main() {
    deque<int> q;
    int Q; cin >> Q;
    int OP, N;
    for (int i = 0; i < Q; i++) {
        cin >> OP;
        switch (OP) {
        case 0:
            cin >> N;
            q.push_front(N);
            break;
        case 1:
            cin >> N;
            q.push_back(N);
            break;
        case 2:
            q.pop_front();
            break;
        case 3:
            q.pop_back();
            break;
        case 4:
            cin >> N;
            cout << q.at(N) << '\n';
            break;
        default:
            break;
        }
    }
}