n = int(input())
a = list(map(int, input().split()))
from itertools import islice 
def batched(iterable, n):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        yield batch

weeks = [sum(e) for e in batched(a,7)]
print(" ".join(map(str, weeks)))
