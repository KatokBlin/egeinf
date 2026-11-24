for x in range(5555,0,-1):
    f=5**150+5**135-x
    k=0
    while f>0:
        if f%5==4:
            k+=1
        f//=5
    if k==134:
        print(x)
        break
