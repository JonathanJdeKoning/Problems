#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    if (N == 0) {
        cout << "1 -1";
    } else if (N == 1) {
        cout << "2 -1";
    } else if (N == -1) {
        cout << "-2 1";
    } else if (N % 2 == 0){
        cout << N/2 << " "  << N/2;
    } else {
        int M = N/2;
        if (N <0) {
            cout << M << " " << M-1;
        } else {
            cout << M << " " << M+1;
        }
    }

}
