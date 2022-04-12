def Body_Mass_Index():
    for _ in range(int(input())):
        h, m = map(int, input().split())
        bmi=h/(m*m)
        if bmi <= 18:
            print("1")
        elif bmi <= 24:
            print("2")
        elif bmi <= 29:
            print("3")
        else:
            print('4')
Body_Mass_Index()

