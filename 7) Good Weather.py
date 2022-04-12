def Good_Weather():
    for _ in range(int(input())):
        reading = map(int,input().split())
        reading = list(reading)
        count=0
        for a in list(reading):
            if a==1:
                count+=1
        if count >= len(reading)-count:
            print("YES")
        else:
            print("NO")
Good_Weather()