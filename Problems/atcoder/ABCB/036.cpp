#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    VV(char, mat, N, N);
    vector<vector<char>> newMat(N, vector<char>(N, 0));

    for (int i = 0; i<N;i++) {
        for(int j = 0; j < N; j++) {
            char cell = mat[i][j];
            newMat[j][N-i-1] = cell;
        }
    }
    for (auto v : newMat) {
        for (auto c : v) {
            cout << c;
        }
        cout << '\n';
    }


}