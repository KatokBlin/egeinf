def f(n):
    s=''
    while n>0:
        s+=str(n%3)
        n//=3
    return s[::-1]
ans=[]
for i in range(1,1000):
    b=f(i)
    if i%5!=0:
        b=b[:-1]+b[0]+f(i%5)
    else:
        b+=b[-1]*2
    if int(b,3)>123:
        ans.append(int(b,3))
print(min(ans))
