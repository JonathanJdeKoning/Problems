#include <bits/stdc++.h>
using namespace std;

void solve() {
    int a,b,c; cin >> a >> b >> c;
    if (((a < b) and (b < c)) or ((a > b) and (b > c))) {cout << "Ordered";} else {cout << "Unordered";}
    cout << endl;
}

int main() {
    int T; cin >> T;
    cout << "Gnomes:" << endl;
    while(T--) {solve();}
}
