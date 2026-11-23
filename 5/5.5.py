def f(n):
    s=''
    while n>0:
        s+=str(n%2)
        n//=2
    return s[::-1]
ans=[]
for i in range(1000):
    b=f(i)
    if i%2==0:
        b='1'+b+'00'
    else:
        b='10'+b+'1'
    if int(b,2)<1000:
        ans.append(i)
print(max(ans))
