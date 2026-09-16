#include <bits/stdc++.h>
using namespace std;

int main() {
    map<char, char> mp = {
        {'a','q'},
        {'b','w'},
        {'c','e'},
        {'d','r'},
        {'e','t'},
        {'f','y'},
        {'g','u'},
        {'h','i'},
        {'i','o'},
        {'j','p'},
        {'k','a'},
        {'l','s'},
        {'m','d'},
        {'n','f'},
        {'o','g'},
        {'p','h'},
        {'q','j'},
        {'r','k'},
        {'s','l'},
        {'t','z'},
        {'u','x'},
        {'v','c'},
        {'w','v'},
        {'x','b'},
        {'y','n'},
        {'z','m'},
        {' ', ' '}
    };
    int N; cin >> N;
    cin.ignore(100, '\n');
    string s;
    getline(cin, s);
    for (char c: s) {
        cout << mp[c];
    }
}
