for x in range(1000):
    f=125**200-5**x+74
    k=0
    while f>0:
        if f%5==4:
            k+=1
        f//=5
    if k==100:
        print(x)
        break
