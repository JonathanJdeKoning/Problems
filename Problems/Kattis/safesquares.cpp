#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_set<int> rows;
    unordered_set<int> cols;

    char board[8][8];
    for (int i =0; i < 8; i++) {
        for (int j = 0; j < 8; j ++) {
            char cell; cin >> cell;
            if (cell == 'R') {
                rows.insert(i);
                cols.insert(j);
                board[i][j] = cell;
            }
        }
    }

    int ans = 64;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (rows.find(i) != rows.end() or cols.find(j) != cols.end()) {
                ans--;
            }
        }
    }
    cout << ans << endl;

}
