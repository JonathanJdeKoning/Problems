#include <bits/stdc++.h>

using namespace std;

int main() {
    char AB, AC, BC;
    cin >> AB >> AC >> BC;
    
    //ASC or DSC
    if (AB == BC) {std::cout << 'B'; exit(0);}
    
    // B is oldest
    if (AB == '<') {
        if (AC == '<' ) {cout << 'C'; exit(0);}
        cout << 'A'; exit(0); 
    //B is youngest
    } else {
        if (AC == '<') {std::cout  << 'A'; exit(0);}
        std::cout << 'C'; exit(0);
    }
}