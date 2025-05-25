s,t,x = map(int, input().split())
if s==t: print("Yes"); exit()
while True:
    if s==t: print("No"); break
    if s==x: print("Yes");break

    s = (s+1)%24
    
