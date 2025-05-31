#include "dekodingTemplate"
int main() {
    string A; cin >> A;
    string B; cin >> B;
    string C; cin >> C;

    vector<string> decks = {A, B, C};
    int currPlayer = 0;

    while (1) {
        if (decks[currPlayer].size() == 0) {cout << ((char)(currPlayer+65)) << endl; return 0;}
        char c = decks[currPlayer].front();
        decks[currPlayer].erase(0,1); 

        if (c == 'a') currPlayer = 0;
        if (c == 'b') currPlayer = 1;
        if (c == 'c') currPlayer = 2;
    }

}
