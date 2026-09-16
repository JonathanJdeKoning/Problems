#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int N; cin >> N;
    if (N == 1) {
        cout << 1; return 0;
    }
    if (N <= 3) {
        cout << "NO SOLUTION";return 0; 
    }

    for (int i = 2; i <= N; i+=2) {
        cout << i << ' ';
    }
    
    for (int i = 1; i <= N; i+=2) {
        cout << i << ' ';
    }
}


