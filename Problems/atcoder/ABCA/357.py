n,d  =  map(int,  input().split())

aliens  =  list(map(int,  input().split()))

t  =  0
for alien in aliens:
    if alien <= d:
        t += 1
        d -= alien
    else:
        break


print(t)
