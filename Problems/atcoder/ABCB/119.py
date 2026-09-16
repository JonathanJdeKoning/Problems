N = int(input())
total = 0
for _ in range(N):
    amount, currency = input().split()
    amount = float(amount)
    if currency  ==  "BTC":
        amount *= 380000
    total += amount

print(total)