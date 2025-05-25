#include <bits/stdc++.h>

using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    if (A+B == 1) {
        if (A == 1) 
            cout << "Yes";
        else
            cout << "No";
    } else {
        cout << "Invalid";
    }
}