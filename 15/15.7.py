def f(x,y):
    return (x>=11) or (3*x<y) or (a>x*y)
for a in range(10000):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        print(a)
        break
