v,a,b,c = map(int,input().split())
d = {0:"F",1:"M",2:"T"}
while True:
    for i, person in enumerate([a,b,c]):
        v -= person
        if v <0: print(d[i]); exit()

