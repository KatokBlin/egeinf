from itertools import*
k=0
for i in product('012345',repeat=6):
    s=''.join(i)
    if s[0]!='0' and s.count('2')==1:
        for c in '135':
            s=s.replace(c,'*')
        if '*2' not in s and '2*' not in s:
            k+=1
print(k)
