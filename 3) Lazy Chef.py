def Lazy_Chef():
    for _ in range(int(input())):
        x, m, d = map(int, input().split())
        print(min(m*x, x+d))
Lazy_Chef()