#include "dekodingTemplate.hpp"

bool isFine(char c) {
    return (c=='a' or c =='t' or c =='c' or c == 'o' or c == 'd' or c == 'e' or c == 'r');
}

int main() {
    STR(S);
    STR(T);

    FOR(i, S.size()) {
        if (S[i] != T[i] and S[i] != '@' and T[i] != '@'){ print("You will lose"); exit(0);}
        if (S[i] == T[i]) continue;
        if (S[i] == '@' and !isFine(T[i])) {print("You will lose"); exit(0);} 
        if (T[i] == '@' and !isFine(S[i])) {print("You will lose"); exit(0);} 

    }
    print("You can win");
}