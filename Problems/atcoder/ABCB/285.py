N = int(input())
S = input()

for gap in range(1, len(S)):
    good = 0
    for j in range(len(S)-gap):
        if S[j] != S[j+gap]:
            good += 1
        else: break
    print(good)
