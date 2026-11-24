def f(n):
    s=''
    while n>0:
        s+=str(n%2)
        n//=2
    return s[::-1]
ans=[]
for i in range(1,1000):
    b=f(i)
    if i%3==0:
        b+=b[-3::]
    else:
        b+=f(i%3*3)
    ans.append((int(b,2),i))
print(sorted(ans))
