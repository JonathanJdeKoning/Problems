N , L = list(map(int, input().split()))

flavors = [L+i for i in range(N)]
flavors.remove(min(flavors, key=lambda x: abs(x)))
print(sum(flavors))