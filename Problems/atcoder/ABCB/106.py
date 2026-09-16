from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
ans = 0
for i in range(1, int(input()) + 1, 2):
    if len(factors(i)) == 8:
        ans += 1
print(ans)
