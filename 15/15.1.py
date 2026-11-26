def f(x,r,l):
    a=r<=x<=l
    p=17<=x<=58
    q=29<=x<=80
    return p<=((q and not a) <= (not p))
ps=[x + dx for x in (17,58,29,80) for dx in (-0.1,0.1)]
ans=[]
for r in ps:
    for l in ps:
        if r<l:
            if all(f(x,r,l) for x in ps):
                ans.append(l-r)
print(min(ans))
