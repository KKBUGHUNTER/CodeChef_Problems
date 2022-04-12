def The_Cooler_Dilemma_1():
    for _ in range(int(input())):
        X, Y, M = map(int, input().split())
        X=X*M
        if X< Y:
            print("YES")
        else:
            print("NO")
The_Cooler_Dilemma_1()


