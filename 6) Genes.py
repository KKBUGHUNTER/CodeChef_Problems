def Genes():
    c = input().split()
    if 'R' in c:
        print("R")
    elif c[0]==c[1]:
        print(c[0])
    elif 'B' in c:
        print('B')
Genes()

