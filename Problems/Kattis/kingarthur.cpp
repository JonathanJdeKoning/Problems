#include <bits/stdc++.h>
using namespace std;

int main() {
    const double PI = 3.141592653589793238462643;
    double d, w; cin >> d >> w;
    double n; cin >> n;
    double circ = PI * d ;
    double roomPer = circ / n;
    if (roomPer >= w) {
        cout << "YES";
    }  else {
        cout << "NO";
    }
}
