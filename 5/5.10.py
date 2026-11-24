def f(n):
    s=''
    while n>0:
        s+=str(n%2)
        n//=2
    return s[::-1]
ans=[]
for i in range(28,1000):
    b=f(i)
    if b.count('1')%2==0:
        b='10'+b[2::]+'0'
    else:
        b='11'+b[2::]+'1'
    ans.append(int(b,2))
print(min(ans))
