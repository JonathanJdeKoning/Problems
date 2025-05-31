#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    VEC(int, A, N);
    double count = ranges::count_if(A, [](int x) {return x > 0;});
    double total = accumulate(all(A), 0);
    int ans = ceil(total/count);
    print(ans);
}