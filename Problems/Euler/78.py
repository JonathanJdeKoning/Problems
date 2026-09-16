from functools import cache


@cache
def p(n):
    if n < 0: return 0
    if n <= 1: return 1

    ans = 0
    
    k = 1
    while True:
        pPart = p(n-gp(k))
        if pPart == 0: break
        ans += ((-1)**(k-1))*pPart
        k += 1

    k = -1
    while True:
        pPart = p(n-gp(k))
        if pPart == 0: break
        ans += ((-1)**(k-1))*pPart
        k -= 1
    return int(ans)%1000000

print

@cache
def gp(m):
    return m*(3*m - 1)//2

x = 1
while True:
    a = p(x)
    #print(x, a)
    if a%1000000 == 0:
        print(x)
        break
    x += 1

