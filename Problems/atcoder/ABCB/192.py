S = input()

o = S[:len(S):2]
e = S[1:len(S):2]

if o == o.lower() and e == e.upper():
    print("Yes")
else:
    print("No")