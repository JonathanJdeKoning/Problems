#include "dekodingTemplate.hpp"

int main() {
    DBL(M);
    double km = M/1000;
    
    if (km < 0.1) {
        print("00");
        exit(0);
    } elif (km <= 5) {
        int newNum = (int)(km*10);
        if (newNum >= 10) {print(newNum); exit(0);}
        cout << 0;
        cout << newNum;
        cout << '\n';
    } elif (km <= 30) {
        print((int)(km + 50));    
    } elif (km <= 70) {
        print((int)((km-30)/5  +80));
    } else {
        print(89);    
    }

}