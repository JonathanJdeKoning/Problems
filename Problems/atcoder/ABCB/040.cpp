#define LOCAL
#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    long long best = 1000000000;
    FOR(i,1, N+1) {
        FOR(j,1, N/i+1) {
            if (i*j > N) {continue;}
            best =min(best, abs(i-j) + (N - i*j));
        }
    }
    print(best);
}