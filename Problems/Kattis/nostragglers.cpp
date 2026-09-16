#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    int people = 0;
    string s, op;
    int num;
    for (int i = 0; i < N; i++) {
        cin >> s >> op >> num;
        if (op == "IN") {
            people += num;
        }  else {
            people -= num;
        }
    }
    cout << ((people > 0) ? to_string(people) : "NO STRAGGLERS");
    
}
