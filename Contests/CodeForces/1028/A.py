def solve():
    gH, fH, gkH, fkH = list(map(int, input().replace(","," ").split()))
    
    gOpp = min(fH, fkH)
    if min(gH, gkH) >= gOpp:
        return "Gellyfish"
    else:
        return "Flower"


for _ in range(int(input())):
    print(solve())