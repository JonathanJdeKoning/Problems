#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int numJewels, numBags;
    cin >> numJewels >> numBags;

    vector<pair<int, int>> jewels;
    for (int i=0; i<numJewels; i++) {
        int jewelMass, jewelValue;
        cin >> jewelMass >> jewelValue;
        jewels.push_back(make_pair(jewelValue, jewelMass));
    }

    sort(jewels.begin(), jewels.end());

    multiset<int> bags;
    for (int i=0; i<numBags; i++) {
        int x; cin >> x;
        bags.insert(x);
    }
    long long ans = 0;
    for (int i = jewels.size()-1; i>=0; i--) {
        auto [jewelValue, jewelMass] = jewels[i];
        auto best = bags.lower_bound(jewelMass);
        if (best == bags.end()) {
            continue;
        }
        ans += jewelValue;
        bags.erase(best);
    }
    cout << ans << '\n';
}


