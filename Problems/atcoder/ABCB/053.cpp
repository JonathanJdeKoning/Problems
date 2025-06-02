#define LOCAL
#include "dekodingTemplate.hpp"

int main() {
    STR(S);
    print(S.find_last_of('Z')-S.find_first_of('A') + 1);
}