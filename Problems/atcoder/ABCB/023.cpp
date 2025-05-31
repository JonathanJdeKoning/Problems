#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    STR(S);
    if (S == "b") {print(0); return 0;}
    string curr = "b";
    int step = 0;
    while (curr.size() <= S.size()) {
        step++;
        if (step % 3 == 1) {
            curr = "a" + curr + "c";
        } elif (step % 3 == 2) {
            curr = "c" + curr + "a";
        } else {
            curr = "b" + curr + "b";
        }
        if (curr == S) {
            print(step);
            return 0;
        }

    }
    print(-1);
}