def RCB_and_Playoffs():
    for _ in range(int(input())):
        X, Y, Z = map(int, input().split())
        Possibility = X + (Z * 2) 
        if Possibility >= Y:
            print("YES")
        else:
            print("NO")
RCB_and_Playoffs()

x,y,z = list(map(int,input().split()))
if((y-x)<=z*2):
    print("YES")
else:
    print("NO")