def f(n):
    s=''
    while n>0:
        s+=str(n%3)
        n//=3
    return s[::-1]
ans=[]
for i in range(4,1000):
    b=f(i)
    if b[-2::]=='10':
        b='2'+b
    else:
        b='1'+b
    if int(b,3)>130:
        ans.append(i)
print(min(ans))
