from itertools import*
k=0
for i in product(sorted('теория'),repeat=6):
    k+=1
    s=''.join(i)
    if s[0]!='р' and s[0]!='т' and s[0]!='я' and s.count('и')>=2 and k%2!=0:
        print(k)
