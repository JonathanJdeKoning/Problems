N = int(input())
items = [int(input()) for _ in range(N)]
items.sort()

total = sum(items)
total -= items.pop() //2

print(total)