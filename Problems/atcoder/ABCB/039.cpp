#define LOCAL
#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    FOR(i, 1001) {
        if (i*i*i*i == N) {
            print(i); return 0;
        } 
    }
}