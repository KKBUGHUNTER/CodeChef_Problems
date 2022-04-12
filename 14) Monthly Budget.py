def Monthly_Budget():
    for _ in range(int(input())):
        x, y =map(int, input().split())
        y= y * 30
        if y <=x:
            print('YES')
        else:
            print('NO')
Monthly_Budget()





