#include "dekodingTemplate.hpp"

int main() {
    STR(s);
    vector<char> A;
    
    for (char c : s) {
        if (c != 'B') {
            A.push_back(c);
        } else {
            if (len(A) == 0) continue;
            A.pop_back();
        }
    }
    for (char c : A) 
        cout << c;
    cout << endl;
}