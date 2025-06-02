#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    if(N%2==0) {
        print(N-1);
    } else {
        print(N+1);
    }
}