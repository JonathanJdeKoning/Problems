#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>

using namespace std;

int main() {
    string s ;
    cin >> s ;
   
    string t;

    for(auto& c: s) {
        if (c != '.') {
            t += c;
        }
    }
    cout << t;

}