#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    int mxSeen = 0;
    for (int i = 0; i < N; i++) {
        string x; cin >> x;
        if (x == "/") {
            cout << (mxSeen + (10-(mxSeen % 10))) << endl; 
        } else {
            mxSeen = max(stoi(x), mxSeen);
            cout << x << endl;
        }

    }
}
