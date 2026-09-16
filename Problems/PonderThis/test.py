from itertools import count, islice
from sympy import factorint
def gen(): return (n for n in count(0) if all(e % 2 == 0 for p, e in factorint(n).items() if p % 3 == 2))

nums = list(islice(gen(), 1000000))
print("Donners")