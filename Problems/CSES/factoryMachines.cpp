#include <bits/stdc++.h>
using namespace std;
#define int long long
int N, T;
vector<int> A;

bool canMakeInTime(int t) {
    int total = 0;
    for (int x : A) {
        total += t / x;
        if (total >= T) return true;
    }
    return false;
}

main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> N >> T;
    A.resize(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    int low = 0; // bad
    int high = 1; // good

    while (not canMakeInTime(high)) {
        high *= 2;
    }    

    while (high > low + 1) {
        int mid = low + (high - low) / 2;
        if (canMakeInTime(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << high;

}


