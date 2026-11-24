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
        b='10'+b
    else:
        b='1'+b+'01'
    if int(b,2)<30:
        ans.append(i)
print(max(ans))
