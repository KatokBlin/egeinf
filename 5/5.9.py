def f(n):
    s=''
    while n>0:
        s+=str(n%2)
        n//=2
    return s[::-1]
ans=[]
for i in range(1,1000):
    b=f(i)
    if i%2==0:
        b+=b[-2::]
    else:
        b='1'+b+'1'
    if int(b,2)>100:
        ans.append(i)
print(min(ans))
