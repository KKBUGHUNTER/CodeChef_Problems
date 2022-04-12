def Chef_and_Vacation_Transportation():
    for _ in range(int(input())):
        x, y, z =map(int, input().split())
        if (x+y) > z:
            print('TRAIN')
        elif (y+x) < z:
            print('PLANEBUS')
        else:
            print('EQUAL')
Chef_and_Vacation_Transportation()