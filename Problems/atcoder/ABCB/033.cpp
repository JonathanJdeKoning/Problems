#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    int total = 0;
    unordered_map<string, int> towns;
    FOR(N) {
        STR(name); INT(pop);
        total += pop;
        towns[name] = pop;
    }

    for (auto name : views::keys(towns)){
        if (towns[name] > total/2) {
            print(name); exit(0);
        }
    } 
    print("atcoder");
}