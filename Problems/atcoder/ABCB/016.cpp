#include "dekodingTemplate.hpp"

int main() {
    INT(A);
    INT(B);
    INT(C);

    if(A + B == C and A-B == C) {
        print("?");
        exit(0);
    }
    if(A+B == C)
        print("+");
    elif (A-B == C)
        print("-");
    else
        print("!");

}