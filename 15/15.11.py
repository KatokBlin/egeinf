def f(x,y,z):
    return ((z%115==0) and (y%78==0) and (x%51==0)) <= ((x*y*z)%a==0)
for a in range(1,1000000):
    if all(f(x,y,z) for x in range(51,1000,51) for y in range(78,1000,78) for z in range(115,1000,115)):
        print(a)
