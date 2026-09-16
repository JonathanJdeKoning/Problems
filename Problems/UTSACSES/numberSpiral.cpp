#include <bits/stdc++.h>
using namespace std;
#define int long long

int query(int y, int x){
    int square = max(y,x) * max(y,x);
    int sy, sx;
    if (max(y,x)%2 == 1) {
        sy = 1;
        sx = max(y,x);
    } else {
        sy = max(y,x);
        sx = 1; 
    }
    int dist = abs(sy-y) + abs(sx -x);
    return square - dist;
}

main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int N; cin >> N;
    for(int i = 0; i <N; i++) {
        int Y, X; cin >> Y >> X;
        cout << query(Y, X);
        cout << '\n';
    }
}


