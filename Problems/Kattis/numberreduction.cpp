#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    int ct = 0;
    while(N != 1) {
        ct++;
        N = ((N%2==0)? N/2 : 3*N+1);
    }
    cout << ct;
}
