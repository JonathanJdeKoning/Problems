#include "dekodingTemplate.hpp"

int main() {
    INT(S);
    int s = S%60;
    S /= 60;
    int m = S%60;
    S /= 60;

    cout << setfill('0') << setw(2) << S;
    cout << ':';
    cout << setfill('0') << setw(2) << m;
    cout << ':';
    cout << setfill('0') << setw(2) << s;
    cout << endl;

}