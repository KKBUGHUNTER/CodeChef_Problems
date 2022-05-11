# cook your dish here
for a in range(int(input())):
    A, B = map(int, input().split())
    if A>B:
        print('A')
    elif B>A:
        print('B')
    else:
        print()