input()
scores = list(map(int, input().split()))
print(sorted([(scores[i],i) for i in range(len(scores))], key = lambda x:x[0])[-2][1]+1)
