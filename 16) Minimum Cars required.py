def Minimum_Cars_required():
    for _ in range(int(input())):
        n =int(input())
        N=n//4
        if n%4==0:
            print(N)
        else:
            print(N+1)
Minimum_Cars_required()
