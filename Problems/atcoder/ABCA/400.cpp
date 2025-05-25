#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    FOR(i, 401) {
        if (i*N == 400) { 
            print(i); exit(0);
        }
    }
    print(-1);

}