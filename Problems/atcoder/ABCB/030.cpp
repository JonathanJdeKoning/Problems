#include "dekodingTemplate"
int main() {
    DBL(H); DBL(M);
    if (H >= 12) {H -= 12;}

    double mAngle = M*6;
    double hAngle = H*30;
    hAngle += 30 * (M/60);
    double angle = abs(hAngle - mAngle);
    if (angle > 180) {
        angle = abs(360);
    }
    print(angle);
}
