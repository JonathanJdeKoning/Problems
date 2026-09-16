#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int N; cin >> N;
    vector<int> A;
    for(int i=0; i < N; i++) {
        A.emplace_back(-1);
        int x;
        cin >> x;
        A.emplace_back(x);
    }
    int Q; cin >> Q;
    vector<bitset<2000>> G(2000);
    int l,r;
    for (int i=1; i<N*2; i+=2) {
        l = i;
        r = i;
        while ((l>=0) and (r<=A.size()-1)) {
            if (A[l] == A[r]) {
                //cout << l << ' ' << r << '\n';
                G[(l-1)/2].set((r-1)/2);
                l -= 2;
                r += 2;
            } else {break;}
        } 
    }
    for (int i = 0; i < N*2; i+=2) {
        l = i-1;
        r = i+1;
        while ((l>=0) and (r<=A.size()-1)) {
            if (A[l] == A[r]) {
                G[(l-1)/2].set((r-1)/2);
                l -= 2;
                r += 2;
            } else {break;}
        }
    }
    int S, E;
    for (int i =0; i < Q; i++) {
        cin >> S >> E;
        S -= 1;
        E -= 1;
        if (G[S].test(E)) {
            cout << 1 << '\n';
        } else {
            cout << 0 << '\n';
        }
    }

}
