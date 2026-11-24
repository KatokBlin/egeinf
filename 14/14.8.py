for x in range(2031,0,-1):
    f=6**260+6**160+6**60-x
    k=0
    while f>0:
        if f%6==0:
            k+=1
        f//=6
    if k==202:
        print(x)
        break
