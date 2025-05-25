#include "dekodingTemplate.hpp"

int main() {
    DBL(N);
    if (N >= 38) {print(1); exit(0);}
    if (N < 37.5) {print(3); exit(0);}
    print(2);
}