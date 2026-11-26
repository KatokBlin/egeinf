def f(x,r,l):
    a=r<=x<=l
    p=66<=x<=67
    o=32<=x<=125
    t=30<=x<=491
    return (not a) <= (p or (not o) or (not t))
ps=[x + dx for x in (66,67,32,125,30,491) for dx in (-0.1,0.1)]
ans=[]
for r in ps:
    for l in ps:
        if r<l:
            if all(f(x,r,l) for x in ps):
                ans.append(l-r)
print(min(ans))
