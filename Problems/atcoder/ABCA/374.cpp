#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>

using namespace std;

int main() {
    string s; cin >> s;
    string sub = s.substr(s.size() - 3);
    if (sub == "san") {
        cout << "Yes";
    } else {
        cout << "No";
    }
}