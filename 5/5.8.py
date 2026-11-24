def f(n):
    s=''
    while n>0:
        s+=str(n%3)
        n//=3
    return s[::-1]
ans=[]
for i in range(4,1000):
    b=f(i)
    if i%5==0:
        b+=b[-3::]
    else:
        b+=f(i%5*5)
    if int(b,3)<5496:
        ans.append(i)
print(max(ans))
