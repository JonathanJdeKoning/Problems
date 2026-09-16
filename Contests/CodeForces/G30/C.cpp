#include <bits/stdc++.h>
using namespace std;
int N, M;
vector<int> B;
vector<int> C;

void solve() {
    cin >> N >> M;
    B.resize(M);
    C.resize(M);
    vector<int> Z;
    vector<pair<int, int>> R;
    multiset<int> S;
    for (int i = 0; i < N; i++) {
        int sword; cin >> sword;
        S.insert(sword);
    }
    
    for (int i = 0; i < M; i++) {cin >> B[i];}
    for (int i = 0; i < M; i++) {cin >> C[i];}

    for (int i = 0; i < M; i++) {
        if (C[i] == 0) {
            Z.push_back(B[i]);
        } else {
            R.push_back(make_pair(B[i], C[i]));
        }
    }
    sort(Z.begin(), Z.end());
    sort(R.begin(), R.end());
    /*
    cout << "Z: ";
    for (int z: Z) {
        cout << z << ", ";
    } cout << '\n';
    cout << "R: ";
    for (auto & [h, l] : R) {
        cout << "(" << h << "," << l <<"), ";
    } cout << '\n';
    cout << "S: ";
    for (auto s : S) {
        cout << s << ", ";
    } cout << '\n';
    */
    
    
    
    int regsKilled = 0;
    for (auto & [health, lvl] : R) {
        auto weakestThatKills = S.lower_bound(health);
        if (weakestThatKills == S.end()) {
            break;
        }
        int newSword = max(*weakestThatKills, lvl);
        S.erase(weakestThatKills);
        S.insert(newSword);
        regsKilled++;
    }

    int zersKilled = 0;
    while ((Z.size() > 0) and (S.begin() != S.end())) {
        if (Z[Z.size() - 1] > *(--S.end())) {
            Z.pop_back();
            continue;
        } else {
            zersKilled++;
            Z.pop_back();
            S.erase((--S.end()));
        }
    }

    cout << regsKilled + zersKilled << '\n';

}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int T; cin >> T;
    while(T--) {
        solve();
    }

}


