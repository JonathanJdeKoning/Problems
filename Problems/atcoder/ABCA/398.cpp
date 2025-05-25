#include "dekodingTemplate.hpp"

int main() {
    INT(N);
    int mid = N/2;
    if (N%2 == 1) {
        FOR(i, N) {
            if (i == mid) {
                cout << '=';
            } else cout << '-';
        }

    } else {
        FOR(i, N) {
            if (i == mid or i == mid-1) {
                cout << '=';
            } else cout << '-';
        }


    }

}