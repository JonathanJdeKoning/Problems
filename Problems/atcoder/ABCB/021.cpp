#include "dekodingTemplate.hpp"

int main() {
   INT(N);
   INT(S); INT(E);
   INT(K);
   VEC(int, A, K);
   set<int> seen;
   seen.insert(S);
   seen.insert(E);

   for (auto i : A) {
        if (seen.contains(i)) {print("NO"); exit(0);}
        seen.insert(i);
   } 
   print("YES");

}