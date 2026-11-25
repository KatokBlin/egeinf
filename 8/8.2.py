from itertools import*
k=0
for i in product('01234',repeat=5):
    s=''.join(i)
    if s[0]!='0' and s.count('2')+s.count('4')+s.count('0')<=3:
        k+=1
print(k)
