class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<pair<int, int>> zeros;
        int R = matrix.size();
        int C = matrix[0].size();

        for (int i=0; i < R; i++) {
            for (int j=0; j < C; j++) {
                if (matrix[i][j] == 0 ) {
                    pair<int, int> loc = {i,j};
                    zeros.push_back(loc);
                }
            }
        }

        for (pair<int, int> p : zeros) {
            int y = p.first;
            int x = p.second;
            for (int j=0; j<C; j++) {
                matrix[y][j] = 0;
            }
            for (int i=0; i<R; i++) {
                matrix[i][x] = 0;
            }
        }
    }
};