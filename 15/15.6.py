def f(x,y):
    return (11<=y) or (7*y<x) or a>x*y
for a in range(10000):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        print(a)
        break
