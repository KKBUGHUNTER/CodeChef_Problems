def passorfail():
    for i in range(int(input())):
        N, X, P = map(int, input().split())
        if (X*3)-(N-X) >=P:
            print("PASS")
        else:
            print("FAIL")
passorfail()

