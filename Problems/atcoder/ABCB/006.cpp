#include "dekodingTemplate.hpp"
int main() {
  
    int mod = 10007;
    INT(N);
    N -= 1;
    vi A = {0,0,1};
    FOR(i,3,1000001) {
        A.eb((A[i-1] + A[i-2] + A[i-3]) % mod);
    }
    print(A[N]);
}
