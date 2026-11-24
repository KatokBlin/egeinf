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
        b+='010'
    else:
        b+=f(i%3*5)
    if int(b,2)>300 and int(b,2)%2==0:
        ans.append((int(b,2),i))
print(min(ans))
