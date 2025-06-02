#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    INT(Q);
    vector<int>A  = vector<int>(N, 0);
    FOR(Q) {
        INT(L);
        INT(R);
        L--;
        R--;
        INT(T);
        FOR(i, L, R+1) {
            A[i] = T;
        }        
    }
    for(auto v : A) {
        print(v);
    }
}