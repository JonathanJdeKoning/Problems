#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_set<char> alph = {'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'};
    string S; cin >> S;
    for (auto c : S) {
        alph.erase(c);
    }
    string out = "";
    for (char c : alph) {
        out += c;
    }
    sort(out.begin(), out.end());

    cout << ((out.size() > 0) ? out : "Good job!");
}
