#define LOCAL
#include "dekodingTemplate.hpp"
#include "utils/math/sieve.hpp"
#include "utils/math/isPrime.hpp"
int main() {
    for (int prime : sieve(1000000000)) {
        int orig = prime;
        
        int digits = (int)ceil(log10(prime));
        //cout << "Prime: "<< prime << ", " << "Size: " << digits << '\n';
        
        for (int mask = 0; mask < 1<<digits; mask++) {
            prime = orig;
            set<int> seen;
            for (int i = 0; i < 10; i++) {
                prime = orig;
                bool good = true;
                //cout << "  Mask: " << bitset<8>(mask).to_string() << '\n'; 
                    
                for (int j = 0; j < digits; j++) {
                    if ((mask >> j) & 1) {
                        
                        int place = (prime%(int)pow(10, j+1)) / pow(10,j);
                        //cout << "    j: " << j << ", x: " << place << '\n'; 
                        
                        prime -= place * pow(10,j);
                        prime +=     i * pow(10,j);
                         
                        int newDigits = (int)ceil(log10(prime));

                        if (newDigits != digits or prime < orig) {
                            good = false;
                            break;
                        }
                    }       
                }
                //cout << "  New Number: " << prime << '\n';
                if (not good) {continue;}
                if (isPrime(prime))
                    seen.insert(prime);
            }
            if (len(seen) == 8) {
                for (auto s: seen) {
                    cout << s << ' ';
                }
                cout << '\n';
            }
        }
    }
}