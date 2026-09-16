#include <bits/stdc++.h>
using namespace std;
#define int long long
int N, K;

int valsLessThan(int k, int m) {
    return min(N, (k-1)/m);
}

int allValsLessThan(int k) {
    int total = 0;
    for (int i = 1; i <= N; i++) {
        total += valsLessThan(k, i); 
    }
    return total;
}

main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> N;
    K = (N*N)/2 + 1;

    int low = 1; //good
    int high = N*N+1; //bad

    while (high > low + 1) {
        int mid = low + (high - low) / 2;
        if (allValsLessThan(mid) < K) {
            low = mid;
        }
        else {
            high = mid;
        }
    }
    cout << low;
}


