#include "dekodingTemplate"
int main() {
    STR(S);
    char curr = S[0];
    int count = 0;
    for (auto c : S) {
        if (c == curr) {
            count++;
        } else {
            cout << curr;
            cout << count;
            curr = c;
            count = 1;
        }
    }
    cout << curr;
    cout << count;
    cout << endl;
}
