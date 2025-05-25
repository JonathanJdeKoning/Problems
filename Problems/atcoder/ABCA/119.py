year,month,day = map(int, input().split("/"))

if year > 2019:
    print("TBD")
elif year < 2019:
    print("Heisei")
else:
    if month < 4:
        print("Heisei")
    elif month > 4:
        print("TBD")
    else:
        if day <= 30:
            print("Heisei")
        else:
            print("TBD")
