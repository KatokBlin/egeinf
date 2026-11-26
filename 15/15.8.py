def f(x):
    return ((x%12==0)<=(x%42!=0)) or (a+x>=4096)
for a in range(1,10000):
    if all(f(x) for x in range(1,10000)):
        print(a)
        break
