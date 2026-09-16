#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    int ans = 0;
    while(N--) {
        int force;
        string result;
        cin >> force >> result;

        if(result == "nej") {
            ans = max(ans, force);
        }

    }
    cout << ans;
}
