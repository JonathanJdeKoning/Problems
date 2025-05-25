#include <iostream>
using namespace std;
int main() {
    int A, B;
    cin >> A >> B;

    if (A == B) {cout << 1; exit(0);}
    if ((max(A,B) - min(A,B)) % 2 == 1) {cout << 2; exit(0);}
    cout << 3;


}