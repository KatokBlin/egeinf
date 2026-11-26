def f(x,r,l):
    a=r<=x<=l
    p=15<=x<=142
    q=38<=x<=167
    return not(q <= ((not a and p)<=(not q)))
ps=[x + dx for x in (15,142,38,167) for dx in (-0.1,0.1)]
ans=[]
for r in ps:
    for l in ps:
        if r<l:
            if all(f(x,r,l)==0 for x in ps):
                ans.append(l-r)
print(min(ans))
