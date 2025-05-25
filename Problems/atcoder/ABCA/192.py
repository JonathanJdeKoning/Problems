n = int(input())
if n%100==0 : print(100); exit()
for i in range(n, n+100):
    if i %100 == 0:
        print(i-n);break
