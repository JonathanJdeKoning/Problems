#line 1 "C:\\Users\\jj720\\Documents\\PythonScripts\\CompetitiveProgramming\\Library\\dekodingTemplate.hpp"
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;

#line 2 "C:\\Users\\jj720\\Documents\\PythonScripts\\CompetitiveProgramming\\Library\\utils\\ioutils.hpp"
void print(auto x) {
  cout << x;
}

void YES(bool t = 1) { print(t ? "YES" : "NO"); }
void NO(bool t = 1) { YES(!t); }
void Yes(bool t = 1) { print(t ? "Yes" : "No"); }
void No(bool t = 1) { Yes(!t); }
void yes(bool t = 1) { print(t ? "yes" : "no"); }
void no(bool t = 1) { yes(!t); }
#line 2 "C:\\Users\\jj720\\Documents\\PythonScripts\\CompetitiveProgramming\\Library\\utils\\shorthand.hpp"
#define all(x) x.begin(), x.end()
#define len(x) ll(x.size())
#define elif else if
#line 12 "C:\\Users\\jj720\\Documents\\PythonScripts\\CompetitiveProgramming\\Library\\dekodingTemplate.hpp"


#line 2 "404.cpp"

int main() {
    string s;
    cin >> s;

    for (char i = 'a'; i <= 'z'; i++) {
        if (s.find(i) == string::npos) { 
            print(i);
            exit(0);
        }
    }

}
