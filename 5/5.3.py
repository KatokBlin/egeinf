def f(n):
    s=''
    while n>0:
        s+=str(n%2)
        n//=2
    return s[::-1]
ans=[]
for i in range(1,1000):
    b=f(i)
    if i%5==0:
        b+='1'
    else:
        b+=f(i%5*2)
    if int(b,2)>102:
        ans.append(int(b,2))
print(min(ans))
