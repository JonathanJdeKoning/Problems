#include "dekodingTemplate.hpp"

int main() {
    VV(char, mat, 4, 4);
    for (auto& v : mat) {
        reverse(all(v));
    } 
    reverse(all(mat));
    for (auto& v : mat) {
        for (char c : v) {
            cout << c << ' ';
        }
        cout << '\n';
    }
}