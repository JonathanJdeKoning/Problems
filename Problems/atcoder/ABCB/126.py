S = input()

fi = int(S[:2])
la = int(S[2:])

if la == 0 and fi == 0:
    exit(print("NA"))

if fi == 0:
    if la <= 12:
        exit(print("YYMM"))
    else:
        exit(print("NA"))

if la == 0:
    if fi <= 12:
        exit(print("MMYY"))
    else:
        exit(print("NA"))

if la > 12 and fi > 12:
    exit(print("NA"))

if la <= 12 and fi <= 12:
    exit(print("AMBIGUOUS"))

if la > 12:
    exit(print("MMYY"))
if fi > 12:
    exit(print("YYMM"))
