#include "dekodingTemplate" 
bool isChoku(string s) {
    if (s == "") {return true;}
    int N = s.size();
    if ((s[N-1] == 'o' or s[N-1] == 'k' or s[N-1] == 'u') and isChoku(s.substr(0,N-1))) return true;
    if (N == 1) return false;
    if (s[N-1] == 'h' and s[N-2] == 'c' and isChoku(s.substr(0,N-2))) return true;
    return false;
}

int main() {
    STR(S);
    YES(isChoku(S));
}
