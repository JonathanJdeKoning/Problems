#include <bits/stdc++.h>
using namespace std;
deque<int> q;
bool rev = false;
map<string, int> ops = {
    {"back", 0},
    {"front", 1},
    {"reverse", 2},
    {"push_back",3},
    {"toFront",4}
};
void operate() {
    string OP; cin >> OP;
    int N;
    switch(ops[OP]) {
    case 0:
        if (q.begin() == q.end()) {cout << "No job for Ada?\n"; return;}

        if (not rev) {
            cout << q.back() << '\n';
            q.pop_back();
        } else {
            cout << q.front() << '\n';
            q.pop_front();
        }
        break;
    case 1:
        if (q.begin() == q.end()) {cout << "No job for Ada?\n"; return;}
        if (not rev) {
            cout << q.front() << '\n';
            q.pop_front();
        } else {
            cout << q.back() << '\n';
            q.pop_back();
        }
        break;
    case 2:
        rev = not rev;
        break;
    case 3:
        cin >> N;
        if (not rev) {q.push_back(N);} else {q.push_front(N);}
        break;
    case 4:
        cin >> N;
        if (not rev) {q.push_front(N);} else {q.push_back(N);}
        break;
    default: break;
    }
    
}

int main() {
    int Q; cin >> Q;
    while(Q--) {
        operate();
    }
}
