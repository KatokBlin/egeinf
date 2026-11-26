def f(x,r,l):
    a=r<=x<=l
    p=15<=x<=33
    q=35<=x<=48
    return ((a) and not q) <= (p or q)
ps=[x + dx for x in (15,33,35,48) for dx in (-0.1,0.1)]
ans=[]
for r in ps:
    for l in ps:
        if r<l:
            if all(f(x,r,l) for x in ps):
                ans.append(l-r)
print(max(ans))
