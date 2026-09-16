#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    int N1; cin >> N1;
    deque<int> A;
    for (int i = 0; i < N1; i++) {
        int x; cin >> x;
        A.push_back(x);
    }

    int N2; cin >> N2;
    deque<int> B;
    for (int i = 0; i < N2; i++) {
        int x; cin >> x;
        B.push_back(x);
    }
    for (int i = 0; i < 2000; i++) {
        if (A.front() > B.front()) {
            A.push_back(B.front());
            B.pop_front();
            A.push_back(A.front());
            A.pop_front();
        } else {
            B.push_back(A.front());
            A.pop_front();
            B.push_back(B.front());
            B.pop_front();
        }
        if (A.size() == N) {
            cout << i+1 << " " << 1;
            return 0;
        }
        if (B.size() == N) {
            cout << i+1 << " " << 2;
            return 0;
        }
    }
    cout << -1;
}
