S = input()
best = 2000
for i in range(len(S)-2):
    best = min(best, abs(753 - int(S[i:i+3])))
print(best)