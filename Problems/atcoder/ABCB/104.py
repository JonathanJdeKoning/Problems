S = input()
if S[0] == "A" and "C" in S[2:-1] and len([x for x in S if x.islower()]) == len(S) - 2:
    print("AC")
else:
    print("WA")