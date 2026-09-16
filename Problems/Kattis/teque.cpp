#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    int N; cin >> N;
    deque<int> teque;
    string OP;
    int X;
    for(int i = 0; i < N; i++) {
        cin >> OP >> X;
        if (OP == "get") {
            cout << teque[X] << '\n';
        }
        
        if (OP == "push_front") {
            teque.push_front(X);
        } 
        
        if (OP == "push_back") {
            teque.push_back(X);
        } 
        
        if (OP == "push_middle") {
            int location = (teque.size()+1)/2;
            teque.insert(teque.begin() + location, X);
        }
        
    }
}


