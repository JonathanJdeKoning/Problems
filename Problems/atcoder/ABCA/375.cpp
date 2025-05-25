#line 1 "A_Seats.cpp"
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>

#line 4 "C:\\Users\\jj720\\Documents\\PythonScripts\\CompetitiveProgramming\\Library\\utils\\ioutils.hpp"

void print(auto s) {
    std::cout << s << '\n';
}

void YES(bool t = 1) { print(t ? "YES" : "NO"); }
void NO(bool t = 1) { YES(!t); }
void Yes(bool t = 1) { print(t ? "Yes" : "No"); }
void No(bool t = 1) { Yes(!t); }
void yes(bool t = 1) { print(t ? "yes" : "no"); }
void no(bool t = 1) { yes(!t); }
#line 2 "C:\\Users\\jj720\\Documents\\PythonScripts\\CompetitiveProgramming\\Library\\utils\\shorthand.hpp"

using ll = long long;

#define all(x) x.begin(), x.end()
#define len(x) ll(x.size())
#define elif else if
#line 8 "A_Seats.cpp"

using namespace std;

int main() {
    int N; cin >> N;
    string s; cin >> s;
    int ans = 0;

    for(int i  = 0 ; i < len(s)-2; i++) {
        if (s[i] == '#' and s[i+1] == '.' and s[i+2] == '#') {
            ans++;
        }
    }
    print(ans);
}
