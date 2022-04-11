def Hardest_Problem_Bet():
    for _ in range(int(input())):
        s1, s2, s3 = map(int, input().split())
        if s3 < s2 and s3 < s1:
            print("Alice")
        elif s2 < s3 and s2 < s1:
            print("Bob")
        else:
            print("Draw")
Hardest_Problem_Bet()

