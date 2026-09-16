N = input()

if len(set(list(N))) == 1: exit(print("Weak"))
for i in range(1,len(N)):
    if ((int(N[i-1]) + 1) % 10) != int(N[i]):  break
    
else:
    exit(print("Weak")) 

print("Strong")