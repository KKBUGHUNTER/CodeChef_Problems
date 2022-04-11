def SUPCHEF():
    for _ in range(int(input())):
        m, n, k = map(int, input().split())
        if m <= (n*k):
            print("NO")
        else:
            print("YES")
SUPCHEF()