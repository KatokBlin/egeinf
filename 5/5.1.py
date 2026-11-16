def f(n):
    s=''
    while n>0:
        s+=str(n%2)
        n//=2
    return s[::-1]
for i in range(1,1000):
    b=f(i)
    c=b.count('1')
    b+=str(c%2)
    c=b.count('1')
    b+=str(c%2)
    if int(b,2)>80:
        print(int(b,2))
        break
