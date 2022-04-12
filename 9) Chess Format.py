def Chess_Format():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        a=a+b
        if a < 3:
            print("1")
        elif a <= 10:
            print("2")
        elif a <= 60:
            print("3")
        else:
            print('4')
Chess_Format()