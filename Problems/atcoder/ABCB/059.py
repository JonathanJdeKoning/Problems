A = input()
B = input()

if len(A) > len(B):
    print("GREATER")
    exit()
if len(A) < len(B):
    print("LESS")
    exit()

if len(A) == len(B):
    for a,b in zip(A, B):
        if a == b: continue
        if int(a) > int(b):
            print("GREATER")
        else:
            print("LESS")
        exit()
print("EQUAL")