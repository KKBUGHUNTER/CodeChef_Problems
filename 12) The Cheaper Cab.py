def The_heaper_Cab():
    for _ in range(int(input())):
        x, y =map(int, input().split())
        if x < y:
            print('FIRST')
        elif y < x:
            print('SECOND')
        else:
            print('ANY')
The_heaper_Cab()

